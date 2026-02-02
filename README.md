# Prédiction-de-la-Gravité-des-Accidents-de-la-Route

Ce projet propose une solution complète de prédiction de la gravité des accidents de la route en France, basée sur un modèle de Machine Learning (LightGBM). L'application est entièrement conteneurisée pour garantir un déploiement reproductible et scalable.

##  Architecture Technique

L'infrastructure repose sur deux services principaux orchestrés par Docker :
- **Backend (API)** : Développé avec FastAPI, il charge le modèle `model_lgb.pkl` et expose un endpoint de prédiction.
- **Frontend (Interface)** : Développé avec Streamlit, il offre une interface utilisateur conviviale pour saisir les données et visualiser les résultats.



---

##  Installation et Déploiement

### Prérequis
- Docker installé sur votre machine
- Docker Compose
