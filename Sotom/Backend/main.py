from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from endpoints.gpt2 import getTextPredict, model, tokenizer
from fastapi.staticfiles import StaticFiles
import os
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Test": "This a test for FastAPI, use /predict with a string to start"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)


@app.get("/predictGPT2")
async def predict_text(input_string: str):
    prediction = getTextPredict(model, tokenizer, input_string)
    return {"prediction": prediction}

app.mount("/images", StaticFiles(directory=os.path.abspath("Python/YOLOv/inference/images/output")), name="images")

@app.get("/images")
@app.get("/images")
def read_images():
    images_dir = "Python/YOLOv/inference/images/output"
    script_path_download = "Python/YOLOv/download-images.py"
    script_path_yolo = "Python/YOLOv/yolov9_imagestraffic.py"
    total_cars_detected_path = "Python/YOLOv/"
    
    try:
        result = subprocess.run(["python", script_path_download], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error ejecutando el script: {e}")

    try:
        result = subprocess.run(["python", script_path_yolo], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error ejecutando el script: {e}")

    images = []
    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                images.append(filename)
    
    # Leer el total de coches detectados desde el archivo
    total_cars_detected = 0
    total_cars_detected_path = os.path.join(total_cars_detected_path, "total_cars_detected.txt")
    if os.path.exists(total_cars_detected_path):
        with open(total_cars_detected_path, "r") as f:
            total_cars_detected = int(f.read().strip())

    return {"images": images, "total_cars_detected": total_cars_detected}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#uvicorn main:app --reload