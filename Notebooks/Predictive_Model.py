from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df_crimenes = pd.read_csv('../Datasets/crimenes_2020_2021_2022.csv')
df_crimenes['CRIMEN_FECHA'] = pd.to_datetime(df_crimenes['CRIMEN_FECHA'], dayfirst=True)

df_crimenes['MES'] = df_crimenes['CRIMEN_FECHA'].dt.month
df_crimenes['DIA_SEMANA'] = df_crimenes['CRIMEN_FECHA'].dt.dayofweek
df_crimenes['ES_FIN_DE_SEMANA'] = df_crimenes['DIA_SEMANA'].isin([5,6]).astype(int)

df_crimenes['AÑO'] = df_crimenes['CRIMEN_FECHA'].dt.year
df_crimenes['TEMPORADA_ALTA'] = df_crimenes['MES'].isin([12, 1]).astype(int)

df_crimenes['CRIMEN_TIPO_SIMPLIFICADO'] = df_crimenes['CRIMEN_TIPO'].replace({
    'robo': 'violento',
    'asalto': 'violento',
    'hurto': 'no_violento',
    'tacha de vehiculo': 'no_violento',
    'robo de vehiculo': 'vehiculo',
    'homicidio': 'homicidio'
})


crimenes_por_distrito = df_crimenes.groupby('LUGAR_DISTRITO').size()
df_crimenes['CANTIDAD_CRIMENES_EN_ZONA'] = df_crimenes['LUGAR_DISTRITO'].map(crimenes_por_distrito)

columnas_a_usar = [
    'VICTIMA_TIPO',
    'VICTIMA_GRUPO_ETARIO',
    'VICTIMA_NACIONALIDAD',
    'LUGAR_PROVINCIA',
    'LUGAR_CANTON',
    'LUGAR_DISTRITO',
    'MES',
    'DIA_SEMANA',
    'ES_FIN_DE_SEMANA'
]

X = df_crimenes[columnas_a_usar]
y = df_crimenes["CRIMEN_TIPO"]

X_encoded = X.copy()
for col in X_encoded.select_dtypes(include='object').columns:
    X_encoded[col] = LabelEncoder().fit_transform(X_encoded[col])

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(class_weight='balanced')
model.fit(X_train, y_train)
preds = model.predict(X_test)

importances = model.feature_importances_
feature_names = X_encoded.columns

feat_imp = pd.Series(importances, index=feature_names)
feat_imp.nlargest(15).plot(kind='barh', figsize=(8,6), title='Top 15 Features')
plt.tight_layout()
plt.show()

cm = confusion_matrix(y_test, preds, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(xticks_rotation=45)
plt.tight_layout()
plt.show()

scores = cross_val_score(model, X_encoded, y, cv=5, scoring='f1_weighted')
print("F1 promedio:", scores.mean())

print(classification_report(y_test, preds))
