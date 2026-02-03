# 🛣️ Road Accident Severity Predictor

[![Docker Hub](https://img.shields.io/badge/DockerHub-Image-blue?logo=docker)](https://hub.docker.com/r/gautierga/accident-app-2)
[![Python](https://img.shields.io/badge/Python-3.13-yellow?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-green?logo=fastapi)](https://fastapi.tiangolo.com/)

## 🎯 Contexte du Projet
En tant que **Data Engineer**, ma mission a été de transformer une application de Machine Learning locale en une infrastructure conteneurisée robuste. Ce projet résout les problèmes d'incompatibilité de versions et garantit un déploiement "en un clic" grâce à Docker.

### Objectifs atteints :
* **Environnement Isolé** : Utilisation d'images Python Slim.
* **Orchestration** : Communication fluide entre l'API (Backend) et Streamlit (Frontend).
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

```

## 🚀 Installation et Démarrage

Avant de commencer, assurez-vous d’avoir installé sur votre machine :

- Docker

Pas besoin de cloner tout le projet : Créez simplement un fichier **docker-compose.yml**


```
services:
  api:
    build:
      context: .
      dockerfile: BACK/Dockerfile
    image: gautierga/accident-app-2:v1
    container_name: accident_api
    ports:
      - "8000:8000"
    networks:
      - accident_network
    command: uvicorn BACK.app:app --host 0.0.0.0 --port 8000
  interface:
    image: gautierga/accident-app-2:v1
    container_name: accident_interface
    ports:
      - "8501:8501"
    networks:
      - accident_network 
    command: streamlit run Front/interface.py --server.address 0.0.0.0
    depends_on:
      - api
    

networks:
  accident_network:
    driver: bridge

```

Ensuite dans votre terminal, dans le dossier ou se trouver le fichier .yaml : exécutez la commande ```docker compose up```


## 🔗 Accès aux Services

Une fois les conteneurs démarrés, les services sont accessibles aux adresses suivantes :

## Interface Streamlit :
👉 http://localhost:8501

## Documentation API (Swagger) :
👉 http://localhost:8000/docs

## Endpoint de vérification de santé :
👉 http://localhost:8000/health

## ⚙️ Orchestration (Docker Compose)

Le fichier docker-compose.yml définit deux services :

- l'Api
  
Exposé sur le port 8000

Fournit le modèle de prédiction


- L'interface

Dépend du service api

Communique avec le backend via l’URL interne :

http://api:8000

## 📊 Utilisation de l’API

L’API accepte des requêtes POST sur l’endpoint /predict avec un payload JSON.

📥 Exemple de requête
```{
  "âge": 25,
  "vitesse Maximale(vma)": 50,
  "Catégorie de route(catr)": autoroute
}```

## 📤 Réponse attendue

Un label de gravité parmi les suivants :

Indemne ✅
Tué ❌
Blessé Hospitalisé 🏥
Blessé Léger 🤕
