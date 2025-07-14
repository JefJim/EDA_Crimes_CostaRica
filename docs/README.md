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

## Hallazgos Relevantes

- Los crímenes más reportados fueron `Hurto`.
- La provincia con más crímenes fue `San José`.
- En `DICIEMBRE-ENERO` se observa un pico de criminalidad constante cada año.
- La mayoría de víctimas son `Adultos mayores`, de nacionalidad `Costarricense`.

---

## Tecnologías Usadas

- Python
- Pandas
- Matplotlib / Seaborn
- JupyterLab

---

## Próximos pasos (opcional)

- Crear un dashboard interactivo con Streamlit o Power BI
- Hacer clustering geográfico con K-Means y coordenadas
- Comparar crimen vs pobreza o ingreso por zona (si se encuentra otro dataset)

---

## ✍️ Autor

- Jefry Jiménez  
- [LinkedIn](https://www.linkedin.com/in/TULINK)  
- [Portafolio (si lo tenés)](https://TUPORTAFOLIO.com)

