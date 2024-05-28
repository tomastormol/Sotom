import pandas as pd
import folium
from folium.plugins import HeatMap
import os

# Rutas absolutas
current_dir_datos_contaminaciones = os.path.abspath('./Sotom/Backend/Python/ObtenerDatosDataBricks/datos_contaminaciones_asc.csv')
#current_dir_datos_contaminaciones = os.path.abspath('./Sotom/Backend/Python/ObtenerDatosDataBricks/datos_contaminaciones.csv')
current_dir_save = os.path.abspath('./Sotom/Backend/Python/PrediccionesContaminacion')

# Leer los datos
data = pd.read_csv(current_dir_datos_contaminaciones)

# Lista de contaminantes
contaminantes = ['PM10']

# Preparar las coordenadas y valores de contaminación
coordenadas_totales = []
for index, row in data.iterrows():
    latitud = row['Latitud']
    longitud = row['Longitud']
    valor_contaminacion = sum(row[contaminante] for contaminante in contaminantes)
    coordenadas_totales.append([latitud, longitud, valor_contaminacion])

# Calcular la ubicación central para el mapa
latitud_total = sum(coor[0] for coor in coordenadas_totales) / len(coordenadas_totales)
longitud_total = sum(coor[1] for coor in coordenadas_totales) / len(coordenadas_totales)

# Crear el mapa con un nivel de zoom inicial menor
valencia_map = folium.Map(location=[latitud_total, longitud_total], zoom_start=13)  # Zoom ajustado

# Añadir el HeatMap
HeatMap(coordenadas_totales, 
        radius=80,
        min_opacity=0.5,
        max_opacity=1,
        ).add_to(valencia_map)

# Guardar el mapa
valencia_map.save(os.path.join(current_dir_save, 'valencia_contaminacion_heatmap_twodaysnext.html'))
print("Creado")
