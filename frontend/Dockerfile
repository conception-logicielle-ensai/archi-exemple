# Étape 1 : Construction de l'application frontend avec Node.js
FROM node:18-alpine AS builder

WORKDIR /app

# Définition de la variable d'environnement pour l'API au moment du build
ARG VITE_API_URL=http://localhost:8000
ENV VITE_API_URL=$VITE_API_URL

# Installation des dépendances
COPY package.json package-lock.json ./
RUN npm install

# Copie du reste du code source
COPY . .

# Construction de l'application avec la variable d'environnement
RUN VITE_API_URL=$VITE_API_URL npm run build

# Étape 2 : Serveur Nginx pour héberger le frontend en production
FROM nginx:stable-alpine

# Copie des fichiers de build du frontend vers le répertoire de Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Exposition du port HTTP
EXPOSE 80

# Lancement du serveur Nginx
CMD ["nginx", "-g", "daemon off;"]