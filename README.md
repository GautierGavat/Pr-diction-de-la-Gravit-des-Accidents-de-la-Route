# 🛣️ Road Accident Severity Predictor

[![Docker Hub](https://img.shields.io/badge/DockerHub-Image-blue?logo=docker)](https://hub.docker.com/r/gautierga/accident-app-2)
[![Python](https://img.shields.io/badge/Python-3.13-yellow?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-green?logo=fastapi)](https://fastapi.tiangolo.com/)

## 🎯 Contexte du Projet
En tant que **Data Engineer**, ma mission a été de transformer une application de Machine Learning locale en une infrastructure conteneurisée robuste. Ce projet résout les problèmes d'incompatibilité de versions et garantit un déploiement "en un clic" grâce à Docker.

### Objectifs atteints :
* **Environnement Isolé** : Utilisation d'images Python Slim.
* **Orchestration** : Communication fluide entre l'API (Backend) et Streamlit (Frontend).
* **Fiabilité** : Mise en place de Healthchecks pour garantir l'ordre de démarrage des services.
* **Distribution** : Image versionnée et disponible sur Docker Hub.

---

## 🏗️ Structure du Projet
```text
.
├── BACK/
│   ├── app.py              # Serveur FastAPI
│   ├── Dockerfile          # Configuration de l'image
│   └── Modèles&Notebooks/  # Modèle LightGBM (.pkl)
├── Front/
│   └── interface.py        # Interface utilisateur Streamlit
├── docker-compose.yml      # Orchestration des conteneurs
├── requirements.txt        # Dépendances communes
└── .env                    # Configuration des variables
