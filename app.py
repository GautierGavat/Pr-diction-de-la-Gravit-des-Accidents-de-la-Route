from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from typing import Dict

app = FastAPI()

# Configuration des labels de sortie
GRAVITE_LABELS = {
    1: "Indemne ✅",
    2: "Tué ❌",
    3: "Blessé Hospitalisé 🏥",
    4: "Blessé Léger 🤕"
}

# Chargement des fichiers sauvegardés
try:
    model = joblib.load('model_lgb.pkl')
    scaler = joblib.load('scaler.pkl')
    features_cols = joblib.load('features_columns.pkl')
except Exception as e:
    print(f"Erreur de chargement des modèles : {e}")

@app.get("/health")
def health():
    return {"status": "online", "model": "LightGBM"}

@app.post("/predict")
def predict(data: Dict[str, float]):
    try:
        # 1. Création d'un DataFrame vide avec toutes les colonnes du modèle
        input_df = pd.DataFrame(0, index=[0], columns=features_cols)
        
        # 2. Remplissage des données numériques directes (vma, age_usager, etc.)
        # et gestion automatique des variables dummy (catr_1, lum_2, etc.)
        for key, value in data.items():
            if key in input_df.columns:
                input_df[key] = value
            # Gestion des colonnes préfixées (ex: l'utilisateur envoie 'lum': 3, on coche 'lum_3.0')
            elif f"{key}_{value}" in input_df.columns:
                input_df[f"{key}_{value}"] = 1
            elif f"{key}_{float(value)}" in input_df.columns:
                input_df[f"{key}_{float(value)}"] = 1

        # 3. Normalisation
        scaled_data = scaler.transform(input_df)
        
        # 4. Prédiction
        pred_num = int(model.predict(scaled_data)[0])
        
        return {
            "prediction": pred_num,
            "label": GRAVITE_LABELS.get(pred_num, "Inconnu"),
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))