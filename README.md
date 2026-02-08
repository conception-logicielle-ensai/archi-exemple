# Archi Exemple

Ce projet illustre les concepts abordés en conception logicielle, avec une application **backend** et **frontend**, ainsi que son **déploiement sur le cloud**.

## Applications

### Backend (`./backend`)
Bilan des deux premières sessions de conception logicielle :
- Git
- Architecture applicative (couches, IoC, SRP)
- Linting et qualité du code
- Tests unitaires
- CI/CD
- Design patterns et bonnes pratiques

### Frontend (`./frontend`)
Bilan du cours 6 de conception logicielle :  
Développement d’une application frontend qui consomme l’API backend.

### Déploiement Cloud (`./kubernetes`)
Contient les scripts Kubernetes nécessaires au déploiement de l’application.

- Un dossier frontend correspondant au frontend déployé sur le sspcloud : https://users-ensai.kub.sspcloud.fr
- Un dossier backend correspondant au backend déployé sur le sspcloud : https://api-users-ensai.kub.sspcloud.fr
---

## Lancer l'application en local avec Docker

### 1. Lancer l'API backend
Depuis la racine du projet, exécuter :
```bash
cd backend
docker build -t backend-app .
docker run -d --name backend-container -p 8000:8000 backend-app
docker ps  # Vérifier que le conteneur tourne
```
L’API sera disponible à :  
- `http://localhost:8000`  
- Swagger UI : `http://localhost:8000/docs`

---

### 2. Lancer l'application frontend
Depuis la racine du projet, exécuter :
```bash
cd frontend
docker build -t frontend-app .
docker run -d -e VITE_API_URL=http://localhost:8000 --name frontend-container -p 8080:80 frontend-app
docker ps  # Vérifier que le conteneur tourne
```
L’application web sera accessible à :  
- `http://localhost:8080`

> L'option -e permet de définir des variable d'environnement au lancement d'une image docker

## Travailler en local avec Docker Compose

Vous pouvez lancer l'application en local directement avec la commande : 
```sh
sudo docker compose up
```

Vous pouvez également travailler en lançant certains modules : 
- Pour travailler sur l'UI:
```sh
sudo docker compose up db backend
```

- Pour travailler sur l'API:
```sh
sudo docker compose up db
```