import pandas as pd
import folium
from folium.plugins import HeatMap

# Cargar el archivo CSV
data = pd.read_csv('/Users/tomas/Desktop/Clase/Proyecto_Final/Python/dataset_osm.csv')

# Lista de contaminantes
contaminantes = ['PM2.5', 'PM10', 'NO2', 'O3', 'SO2', 'CO']

# Crear una lista para almacenar todas las coordenadas
coordenadas_totales = []

# Sumar los valores de contaminación de todos los puntos
for index, row in data.iterrows():
    latitud = row['Latitud']
    longitud = row['Longitud']
    # latitud = 39.4456696664508
    # longitud = -0.3698880681584703
    valor_contaminacion = sum(row[contaminante] for contaminante in contaminantes)
    coordenadas_totales.append([latitud, longitud, valor_contaminacion])

# Sumar las coordenadas para obtener un único punto central
latitud_total = sum(coor[0] for coor in coordenadas_totales) / len(coordenadas_totales)
longitud_total = sum(coor[1] for coor in coordenadas_totales) / len(coordenadas_totales)
valor_total = sum(coor[2] for coor in coordenadas_totales)

# Crear el mapa centrado en la ubicación media de los puntos
valencia_map = folium.Map(location=[latitud_total, longitud_total], zoom_start=14)

# Añadir el HeatMap al mapa con los datos combinados
HeatMap(coordenadas_totales, 
        radius=80,
        min_opacity=0.5,
        max_opacity=1,
        ).add_to(valencia_map)

# Guardar el mapa como HTML
valencia_map.save('valencia_contaminacion_heatmap.html')
