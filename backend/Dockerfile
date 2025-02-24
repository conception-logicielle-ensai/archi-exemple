# Utilisation de l'image officielle Python 3.10 comme base
FROM python:3.10

# Définition du répertoire de travail
WORKDIR /code

# Copier tout le code du backend dans le conteneur
COPY . /code/
ENV APP_TITLE=UserAPIEnsai
# Installation des dépendances sans mise en cache pour un build plus léger
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Commande pour démarrer l'application
CMD ["python", "main.py"]