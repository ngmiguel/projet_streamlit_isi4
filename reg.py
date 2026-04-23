import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import time

# Chargement du modèle pré-entraîné
with open('reg.pkl', 'rb') as f:
    model = pickle.load(f)

# Titre et mise en page
st.set_page_config(page_title="Prediction de Charges Medicales")
st.title("Prédiction de Charges Médicales")
st.markdown("Remplis les informations ci-dessous pour prédire les charges médicales.")

# Ajout d'annimation de chargement
with st.spinner('Chargement du modèle...'):
    time.sleep(2)  # Simule un temps de chargement

# Entrée des données utilisateur
col1, col2 = st.columns(2)
with col1:
    age = st.slider("Âge",18,100,30)
with col2:
    sex = st.selectbox("Sexe", ["Male", "Female"])

col3, col4 = st.columns(2)
with col3:
    bmi = st.number_input("Indice de Masse Corporelle (BMI)", 10,50,25)
with col4:
    children = st.slider("Nombre d'enfants", 0, 5,1)

col5, col6 = st.columns(2)
with col5:
    smoker = st.selectbox("Fumeur", ["Yes", "No"])
with col6:
    region = st.selectbox("Région", ["northeast", "northwest", "southeast", "southwest"])

# Encodage des Regions
region_dict = {"southwest": 0.24308153, "southeast":0.27225131, "northwest":0.24233358, "northeast":0.27225131}
region_encoded = region_dict[region]

# Encodage du Sexe
le_sex = LabelEncoder()
le_sex.fit(["Male", "Female"])
sex_encoded = le_sex.transform([sex])[0]

# Encodage du Fumeur
le_smoker = LabelEncoder()
le_smoker.fit(["Yes", "No"])
smoker_encoded = le_smoker.transform([smoker])[0]

# Préparation des données pour la prédiction
input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

# Prédiction
if st.button("Prédire les Charges Médicales"):
    with st.spinner('Calcul en cours...'):
        prediction = model.predict(input_data)
        time.sleep(2)  # Simule un temps de calcul
    st.success("Prédiction terminée!")
    st.markdown(f"### Charges Médicales Prédites : **${prediction[0]:.2f}**")
    st.balloons()