# Utilisez une image Python de base
FROM python:3.11

# Copiez les fichiers de votre application dans le conteneur
COPY . /app

# Définissez le répertoire de travail
WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Installez les dépendances de votre application
#RUN pip install -r python-dependencies.txt

# Définissez les variables d'environnement Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exposez le port 5000 pour accéder à l'application Flask
EXPOSE 5000

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD [ "flask", "run" ]
