import streamlit as st
import requests

# Configuration de la page
st.set_page_config(page_title="Prédiction Gravité Accident", page_icon="🚗", layout="centered")

# CSS personnalisé pour améliorer le look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Analyse de Risque d'Accident")
st.write("Saisissez les caractéristiques pour prédire la gravité potentielle.")

# Formulaire principal
with st.form("accident_form"):
    st.subheader("📍 Environnement et Route")
    col1, col2 = st.columns(2)
    
    with col1:
        vma = st.number_input("Vitesse maximale (vma)", min_value=0, max_value=130, value=80)
        catr = st.selectbox("Catégorie de route (catr)", options=[1, 2, 3, 4], 
                            format_func=lambda x: {1:"Autoroute", 2:"Nationale", 3:"Départementale", 4:"Voie communale"}[x])
        lum = st.selectbox("Lumière (lum)", options=[1, 2, 3, 4, 5], 
                           format_func=lambda x: {1:"Plein jour", 2:"Crépuscule/Aube", 3:"Nuit sans éclairage", 4:"Nuit éclairée", 5:"Nuit éclairage éteint"}[x])

    with col2:
        agg = st.selectbox("Localisation (agg)", options=[1, 2], format_func=lambda x: "Hors agglomération" if x==1 else "En agglomération")
        # On simule jour/soir/nuit via une heure de saisie
        heure = st.slider("Heure de l'accident", 0, 23, 14)
        moment = 1 if 6 <= heure <= 18 else 2 if 19 <= heure <= 22 else 3 # 1:Jour, 2:Soir, 3:Nuit

    st.divider()
    st.subheader("👤 Profil de l'Usager")
    col3, col4 = st.columns(2)
    
    with col3:
        age = st.number_input("Âge de l'usager", min_value=0, max_value=100, value=25)
    with col4:
        sexe = st.selectbox("Sexe", options=[1, 2], format_func=lambda x: "Homme" if x==1 else "Femme")

    submitted = st.form_submit_button("LANCER LA PRÉDICTION")

# Traitement du clic
if submitted:
    # On prépare les données pour l'API
    # Assure-toi que les clés correspondent aux noms de tes colonnes avant get_dummies
    payload = {
        "vma": float(vma),
        "age_usager": float(age),
        "sexe": float(sexe),
        "catr": float(catr),
        "lum": float(lum),
        "agg": float(agg),
        "moment": float(moment) # Ta variable personnalisée
    }
    
    try:
        with st.spinner('Calcul du risque en cours...'):
            response = requests.post("http://accident_api:8000/predict", json=payload)
            result = response.json()
            
            label = result['label']
            
            # Affichage stylisé selon le résultat
            st.markdown("### Résultat de l'analyse :")
            if "Tué" in label:
                st.error(f"### {label}")
                st.info("⚠️ Risque critique détecté. Facteurs probables : Vitesse et manque de protection.")
            elif "Hospitalisé" in label:
                st.warning(f"### {label}")
            elif "Indemne" in label:
                st.success(f"### {label}")
            else:
                st.info(f"### {label}")

    except Exception as e:
        st.error("Impossible de contacter l'API. Vérifiez que la commande 'uvicorn app:app' est lancée.")