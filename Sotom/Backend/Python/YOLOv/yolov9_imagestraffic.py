import os
import numpy as np
from ultralytics import YOLO
import cv2
import random

current_dir_coco = os.path.dirname(os.path.abspath(__file__))
coco_txt_path = os.path.join(current_dir_coco, "utils", "coco.txt")

current_dir_traffic = os.path.dirname(os.path.abspath(__file__))
traffic_txt_path = os.path.join(current_dir_coco, "utils", "traffic.txt")

current_dir_dgt_images = os.path.dirname(os.path.abspath(__file__))
dgt_images_txt_path = os.path.join(current_dir_dgt_images, "inference", "images", "input", "dgt_images")

current_dir_dgt_images_output = os.path.dirname(os.path.abspath(__file__))
dgt_images_output_txt_path = os.path.join(current_dir_dgt_images_output, "inference", "images", "output")

# Abre el archivo coco.txt
with open(coco_txt_path, "r") as fileCocoObjects:
    data = fileCocoObjects.read()
with open(traffic_txt_path, "r") as fileTrafficObjects:
    trafficData = fileTrafficObjects.read()

# Obtenemos objetos separando por newline ('\n')
class_list = data.split("\n")
class_list_traffic = trafficData.split("\n")

# Generar colores aleatorios para cada objeto
detection_colors = []
for i in range(len(class_list)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    detection_colors.append((b, g, r))

# Cargar modelo preentrenado YOLO
model = YOLO("../yolov9c.pt")

# Valores para redimensionar los frames del video
frame_wid = 640
frame_hyt = 480

def listar_contenido_carpeta(ruta):
    contenido = []
    for elemento in os.listdir(ruta):
        ruta_elemento = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_elemento):
            contenido.append(ruta_elemento)
        elif os.path.isdir(ruta_elemento):
            contenido.extend(listar_contenido_carpeta(ruta_elemento))
    return contenido

# Inicializar el contador de coches
total_cars_detected = 0

# Llamada a la función para listar el contenido de la carpeta
contenido_carpeta = listar_contenido_carpeta(dgt_images_txt_path)

for image_ruta in contenido_carpeta:
    cap = cv2.imread(image_ruta)
    if cap is None:
        print(f"Error al cargar la imagen {image_ruta}")
        continue

    # Capturar frame a frame
    frame = np.array(cap)

    # Procesar frame
    frame = cv2.resize(frame, (frame_wid, frame_hyt))
    # Predict sobre la imagen
    detect_params = model.predict(source=[frame], conf=0.25, save=False)

    # Si se está utilizando GPU (cuda) se debe pasar la información antes a la CPU para poder convertir a numpy
    parametrosDetectados = detect_params[0].cpu() if model.device.type == 'cuda' else detect_params[0]

    if len(parametrosDetectados.numpy()) != 0:  # Si es 0 no se ha detectado nada
        for objetoDetectado in parametrosDetectados.boxes:
            clsID = int(objetoDetectado.cls.numpy()[0])  # clase de objeto (número)
            if class_list[clsID] in class_list_traffic:
                if class_list[clsID] == "car":  # Asegúrate de que la clase "car" está en tu lista
                    total_cars_detected += 1

                conf = round(objetoDetectado.conf.numpy()[0], 3)  # probabilidad/confianza
                x1, y1, x2, y2 = objetoDetectado.xyxy.numpy()[0]  # bounding box
                cv2.rectangle(
                    frame,  # imagen sobre la que dibujar cuadro
                    (int(x1), int(y1)),  # x, y del rectángulo deben ser enteros
                    (int(x2), int(y2)),  # x2=x1+ancho, y2=y1+alto
                    detection_colors[clsID],  # color de la clase del objeto
                    3,
                )
                # Dibujar cajita con el nombre de la clase (no el número) y la probabilidad
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(
                    frame,
                    class_list[clsID],
                    (int(x1), int(y1) - 10),  # coordenadas numéricas no decimales
                    font,
                    1,
                    (255, 255, 255),
                    2,
                )

        # Guardar frame
        if not os.path.exists(dgt_images_output_txt_path):
            os.makedirs(dgt_images_output_txt_path)
        output_image_path = os.path.join(dgt_images_output_txt_path, os.path.basename(image_ruta))
        cv2.imwrite(output_image_path, frame)
        print(f"Imagen guardada en {output_image_path}")

# Guardar el total de coches detectados en un archivo
total_cars_detected_path = os.path.join(current_dir_dgt_images_output, "total_cars_detected.txt")
with open(total_cars_detected_path, "w") as f:
    f.write(str(total_cars_detected))
