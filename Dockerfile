# Utiliser une image de base Python 3.12
FROM python:3.12-slim

# Installer Poetry
RUN pip install poetry

# Définir le répertoire de travail
WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false

# Copier les fichiers dans le conteneur
COPY poetry.lock pyproject.toml ./

# Installer les dépendances sans installer le projet lui-même
RUN poetry install --no-root

# Copier le reste des fichiers (notamment ton application Flask)
COPY . .

# Exposer le port Flask
EXPOSE 8080

# Lancer l'application
CMD ["bash", "-c", "flask --app app/mon_api --debug run --host 0.0.0.0 -p 8080"]
