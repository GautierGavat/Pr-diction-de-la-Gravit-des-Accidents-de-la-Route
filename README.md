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
```

## 🚀 Installation et Démarrage

Avant de commencer, assurez-vous d’avoir installé sur votre machine :

- Docker

- Docker Compose

## 🐳 Déploiement de l’Application

Option 1 : Déploiement via Docker Hub (Production)

Pour lancer l’application sans cloner le code source, utilisez directement l’image distante :

docker-compose up -d

## Option 2 : Build Local (Développement)

Pour modifier le code source et reconstruire l’image localement :

docker-compose up --build

## 🔗 Accès aux Services

Une fois les conteneurs démarrés, les services sont accessibles aux adresses suivantes :

## Interface Streamlit :
👉 http://localhost:8501

## Documentation API (Swagger) :
👉 http://localhost:8000/docs

## Endpoint de vérification de santé :
👉 http://localhost:8000/health

🛠️ Détails Techniques
🐍 Dockerfile


L’image Docker est construite à partir de python:3.13-slim et inclut :
libgomp1
Requis pour l’exécution du modèle LightGBM.
curl
Utilisé par Docker pour effectuer les healthchecks.

## Sécurité
L’application s’exécute avec l’utilisateur non-privilégié cableXLR, conformément aux bonnes pratiques de production.

## ⚙️ Orchestration (Docker Compose)

Le fichier docker-compose.yml définit deux services :

- l'Api
Exposé sur le port 8000

Fournit le modèle de prédiction

Inclut un healthcheck sur l’endpoint /health

- L'interface

Dépend du service api

Communique avec le backend via l’URL interne :
http://api:8000

## 📊 Utilisation de l’API

L’API accepte des requêtes POST sur l’endpoint /predict avec un payload JSON.

📥 Exemple de requête
{
  "age": 25,
  "vitesse": 50,
  "meteo_soleil": 1
}

## 📤 Réponse attendue

Un label de gravité parmi les suivants :

Indemne ✅
Tué ❌
Blessé Hospitalisé 🏥
Blessé Léger 🤕
