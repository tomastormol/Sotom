from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Ruta al directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo HTML
html_file_path = os.path.join(current_dir, "valencia_contaminacion_heatmap_twodaysnext.html")

# Ruta para guardar la captura de pantalla
screenshot_path = os.path.join(current_dir, "captura.png")

# Configurar opciones de Chrome para el modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)

# Crear el navegador Chrome
driver = webdriver.Chrome(options=chrome_options)

# Abrir el archivo HTML local
driver.get("file:///" + html_file_path)

# Esperar a que la página se cargue completamente (ajustar si es necesario)
time.sleep(2)

# Tomar la captura de pantalla y guardarla
driver.save_screenshot(screenshot_path)

# Cerrar el navegador
driver.quit()

print(f"Captura de pantalla guardada en: {screenshot_path}")
