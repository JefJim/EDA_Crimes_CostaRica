#  Análisis de Crímenes en Costa Rica (2020–2022)

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre los crímenes reportados en Costa Rica durante los años 2020, 2021 y 2022. El objetivo es identificar patrones temporales, geográficos y demográficos que permitan entender mejor el comportamiento delictivo en el país.

---

## Estructura del Proyecto

- `Notebooks/EDA_Crimenes_CR.ipynb`: Notebook principal con todo el análisis exploratorio.
- `Datasets/crimenes_2020_2021_2022.csv`: Dataset original 

---

## 📌 Dataset

- **Fuente**: Kaggle – [Crime data in Costa Rica](https://www.kaggle.com/datasets/isaacpm21/crime-data-in-costa-rica-years-2020-to-2022)
- **Columnas principales**:
  - `CRIMEN_TIPO`, `CRIMEN_FECHA`, `VICTIMA_GRUPO_ETARIO`, `LUGAR_PROVINCIA`, `LUGAR_CANTON`, `LUGAR_DISTRITO`
  **Cobertura**: Años 2020, 2021 y 2022
  - Todas las columnas son categóricas
  - Dataset no contiene valores nulos

---

## Análisis Exploratorio (EDA)

**Preguntas clave abordadas:**

- ¿Cuáles son los crímenes más frecuentes en Costa Rica?
- ¿Qué provincias tienen mayor incidencia delictiva?
- ¿Cómo varía el crimen a lo largo de los meses y años?
- ¿Qué perfil tienen las víctimas más comunes?

**Gráficas incluidas**:
- Crímenes por tipo y por provincia
- Evolución temporal de crímenes por mes/año
- Distribución de víctimas por grupo etario y nacionalidad

---

## Mapa Interactivo + Clustering Geográfico

- Se necesita instalar **Folium** con el comando `pip install folium` y **Geopandas** para convertir un archivo geojson a GeoDataFrame `pip install geopandas`

Se construyó un **mapa interactivo con Folium** que incluye:
- Un **círculo por distrito** con tamaño proporcional a la cantidad de crímenes
- **Clusters geográficos** usando KMeans (agrupación de distritos por cercanía)
- En cada popup se muestra:
  - Nombre del distrito
  - Total de crímenes reportados
  - Número de cluster asignado
  - **Top 4 tipos de crímenes** más frecuentes en ese distrito
  Mapa generado: [`mapa_crimenes_con_top4.html`](../Notebooks/mapa_crimenes_con_top4.html)

---

## Hallazgos Relevantes

- Los crímenes más reportados fueron `Hurto`.
- La provincia con más crímenes fue `San José`.
- En `DICIEMBRE-ENERO` se observa un pico de criminalidad constante cada año.
- La mayoría de víctimas son `Adultos mayores`, de nacionalidad `Costarricense`.

---

## Tecnologías Usadas

- Python
- Pandas & GeoPandas
- Matplotlib / Seaborn
- Scikit-learn (KMeans)
- Folium (mapas interactivos)
- JupyterLab

---

## ¿Cómo correr este proyecto?

Cloná el repositorio:
```bash
  git clone https://github.com/JefJim/EDA_Crimes_CostaRica.git
  pip install folium
  pip install geopandas
  cd Notebooks
  python Clustering_K-Means.py
```

O bien, abrí directamente el mapa generado "../Notebooks/mapa_crimenes_con_top4.html" en tu navegador favorito.

---

## ✍️ Autor

- Jefry Jiménez  
- [LinkedIn](https://www.linkedin.com/in/jefry-jim%C3%A9nez-rocha-881b171b9/)  
- [Portafolio](https://github.com/JefJim)

