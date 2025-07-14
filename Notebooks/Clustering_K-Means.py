import pandas as pd
import geopandas as gpd
from sklearn.cluster import KMeans
import folium
from collections import defaultdict

# Cargar crimenes
df_crimenes = pd.read_csv('../Datasets/crimenes_2020_2021_2022.csv')

# Cargar geojson
gdf = gpd.read_file('../Datasets/Distritos_de_Costa_Rica.geojson')


gdf_utm = gdf.to_crs(epsg=32616)
gdf_utm['centroide'] = gdf_utm.geometry.centroid

gdf_centroides = gpd.GeoDataFrame(gdf_utm, geometry='centroide', crs='EPSG:32616')
gdf_centroides = gdf_centroides.to_crs(epsg=4326)

# Extraer centroides precisos
gdf_centroides['LATITUD'] = gdf_centroides.geometry.y
gdf_centroides['LONGITUD'] = gdf_centroides.geometry.x

# Normalizar texto
for col in ['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO']:
    df_crimenes[col] = df_crimenes[col].str.upper().str.strip()

for col in ['NOM_PROV', 'NOM_CANT', 'NOM_DIST']:
    gdf[col] = gdf[col].str.upper().str.strip()

# Merge para agregar coordenadas a los crímenes
df_geo_crimenes = df_crimenes.merge(
    gdf_centroides[['NOM_PROV', 'NOM_CANT', 'NOM_DIST', 'LATITUD', 'LONGITUD']],
    left_on=['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO'],
    right_on=['NOM_PROV', 'NOM_CANT', 'NOM_DIST'],
    how='left'
)

# Agrupar por distrito para clustering
grouped = df_geo_crimenes.groupby(
    ['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO', 'LATITUD', 'LONGITUD']
).size().reset_index(name='CANTIDAD_CRIMENES')

# Agrupar por distrito y tipo de crimen
top_crimenes = (
    df_geo_crimenes
    .groupby(['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO', 'CRIMEN_TIPO'])
    .size()
    .reset_index(name='CANTIDAD')
)
# Obtener top 4 por distrito
top4_crimenes = (
    top_crimenes
    .sort_values(['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO', 'CANTIDAD'], ascending=[True, True, True, False])
    .groupby(['LUGAR_PROVINCIA', 'LUGAR_CANTON', 'LUGAR_DISTRITO'])
    .head(4)
)

crimenes_dict = defaultdict(list)
for _, row in top4_crimenes.iterrows():
    key = (row['LUGAR_PROVINCIA'], row['LUGAR_CANTON'], row['LUGAR_DISTRITO'])
    crimenes_dict[key].append((row['CRIMEN_TIPO'], row['CANTIDAD']))

# Aplicar KMeans
X = grouped[['LATITUD', 'LONGITUD']]
kmeans = KMeans(n_clusters=5, random_state=42)
grouped['CLUSTER'] = kmeans.fit_predict(X)
grouped = grouped.dropna(subset=['LATITUD', 'LONGITUD'])

m = folium.Map(location=[9.7489, -83.7534], zoom_start=7)
colors = ['red', 'blue', 'green', 'purple', 'orange']

for _, row in grouped.iterrows():
    key = (row['LUGAR_PROVINCIA'], row['LUGAR_CANTON'], row['LUGAR_DISTRITO'])
    crimenes = crimenes_dict.get(key, [])
    
    # Crear resumen HTML
    crimenes_html = "".join(
        f"<li>{tipo}: {cant}</li>" for tipo, cant in crimenes
    )
    
    popup_html = f"""
    <strong>Distrito:</strong> {row['LUGAR_DISTRITO']}<br>
    <strong>Crímenes totales:</strong> {int(row['CANTIDAD_CRIMENES'])}<br>
    <strong>Cluster:</strong> {int(row['CLUSTER'])}<br><br>
    <strong>Top 4 crímenes:</strong>
    <ul>{crimenes_html}</ul>
    """

    folium.CircleMarker(
        location=[row['LATITUD'], row['LONGITUD']],
        radius=6 + row['CANTIDAD_CRIMENES'] / 100,
        color=colors[int(row['CLUSTER']) % len(colors)],
        fill=True,
        fill_opacity=0.8,
        popup=folium.Popup(popup_html, max_width=300)
    ).add_to(m)

m.save("mapa_crimenes_con_top4.html")
