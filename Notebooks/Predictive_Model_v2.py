
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


df = pd.read_csv("../Datasets/crimenes_2020_2021_2022.csv")
df['CRIMEN_FECHA'] = pd.to_datetime(df['CRIMEN_FECHA'], dayfirst=True)

df['MES'] = df['CRIMEN_FECHA'].dt.month
df['DIA_SEMANA'] = df['CRIMEN_FECHA'].dt.dayofweek
df['ES_FIN_DE_SEMANA'] = df['DIA_SEMANA'].isin([5, 6]).astype(int)
df['TEMPORADA_ALTA'] = df['MES'].isin([12, 1]).astype(int)


features = [
    'VICTIMA_TIPO',
    'VICTIMA_GRUPO_ETARIO',
    'VICTIMA_NACIONALIDAD',
    'LUGAR_PROVINCIA',
    'LUGAR_CANTON',
    'LUGAR_DISTRITO',
    'MES',
    'DIA_SEMANA',
    'ES_FIN_DE_SEMANA',
    'TEMPORADA_ALTA'
]

X = df[features]
y = df['CRIMEN_TIPO']

cat_cols = X.select_dtypes(include='object').columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)],
    remainder='passthrough'
)

X_encoded = preprocessor.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("F1 promedio:", cross_val_score(model, X_encoded, y, cv=5, scoring='f1_weighted').mean())
print(classification_report(y_test, preds))

cm = confusion_matrix(y_test, preds, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(xticks_rotation=45)
plt.tight_layout()
plt.show()

importances = model.feature_importances_
feature_names = preprocessor.get_feature_names_out()
feat_imp = pd.Series(importances, index=feature_names)
feat_imp.nlargest(20).plot(kind='barh', figsize=(8,6), title='Top 20 Features')
plt.tight_layout()
plt.show()
