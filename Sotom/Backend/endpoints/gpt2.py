import string
import torch
import re

from transformers import GPT2LMHeadModel, AutoTokenizer

dir = "./models/gpt2"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = GPT2LMHeadModel.from_pretrained(dir)
tokenizer = AutoTokenizer.from_pretrained(dir, bos='<bos>', eos='<eos>', pad='pad')

stations = ["Avenida Francia", "Bulevard Sud", "Conselleria Meteo", "Moli del Sol", "Nazaret Meteo", 
            "Pista Silla", "Politecnico", "Puerto Moll Trans Ponent", "Puerto Valencia", "Puerto llit antic Turia", 
            "Valencia Centro", "Valencia Olivereta", "Viveros"]


def getTextPredict(model, tokenizer, data):
    # Agregar <bos> al inicio y <eos> al final
    inputText = data
    data = f"<bos> {data} <eos>"
    
    # Buscar fechas en el formato YYYY-mm-dd y añadir una coma después
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    data = re.sub(pattern, r"\g<0><|Fecha|>", data)

    for station in stations:
        data = re.sub(rf"\b{station}\b", f"{station}<|Estacion|>", data, flags=re.IGNORECASE)

    print("-----")
    print(data)
    print("-----")
    
    generated = torch.tensor(tokenizer.encode(data)).unsqueeze(0)
    generated = generated.to(device)

    output = model.generate(generated, do_sample=True, top_k=1, max_length=300, top_p=0.95, num_return_sequences=1)
    output =  tokenizer.decode(output[0], skip_special_tokens=True)
    output = output.split("grados")[0] + "grados"
    output = output.replace("<|Fecha|>", "")
    output = output.replace("<|Estacion|>", "")
    output = output.replace("|>", "")
    output = output.replace("<|", "")
    print("--- Output ---")
    print(output)
    output = output.replace(inputText, "")

    return output