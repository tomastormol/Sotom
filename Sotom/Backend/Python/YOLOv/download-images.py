from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os
import mimetypes
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Obtiene la ruta absoluta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define la ruta absoluta de la carpeta donde se guardarán las imágenes
folder_name = os.path.join(current_dir, "inference", "images", "input", "dgt_images")
os.makedirs(folder_name, exist_ok=True)

# Configura las opciones de Chrome para el modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless
chrome_options.add_argument("--disable-gpu")  # Necesario para Windows
chrome_options.add_argument("--no-sandbox")  # Necesario para Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Necesario para Docker

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.dgt.es/conoce-el-estado-del-trafico/camaras-de-trafico/?pag=1&prov=46&carr=V-30")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

images = soup.find_all("img")

img_count = 1

for img in images:
    img_url = img.get("src")
    if img_url and img_url.startswith("https://"):
        print("Descargando imagen:", img_url)
        img_response = requests.get(img_url)
        img_data = img_response.content
        img_type = img_response.headers.get("content-type")
        img_ext = mimetypes.guess_extension(img_type)
        img_name = str(img_count) + img_ext
        img_path = os.path.join(folder_name, img_name)
        with open(img_path, "wb") as f:
            f.write(img_data)
        img_count += 1

driver.quit()
