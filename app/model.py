
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account


KEYFILE = "/home/ensai/COURS/DataOps/Google Cloud Platform/ensai-2025-cb17d74eb8b2.json"
credentials = service_account.Credentials.from_service_account_file(KEYFILE)


# data = pandas_gbq.read_gbq("SELECT preusuel as name, sexe as gender, SUM(CAST(nombre)) as total FROM ml.prenoms", project_id="ensai-2025", credentials = credentials)
data = pandas_gbq.read_gbq("SELECT * FROM ml.prenoms", project_id="ensai-2025", credentials = credentials)

print(data)




import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import pickle



# 2. Encodage du genre
label_encoder = LabelEncoder()
data['genre_encoded'] = label_encoder.fit_transform(data['sexe'])
y = data['genre_encoded']

# 3. Feature engineering - Vectorisation des prénoms
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))
X = vectorizer.fit_transform(data['preusuel'])

# 4. Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entraîner le modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Évaluer le modèle
score = model.score(X_test, y_test)
print(f"Score du modèle : {score:.2f} 🐾")

# 6. Sauvegarder le modèle dans un fichier .bin
with open("model_prenoms.bin", "wb") as f:
    pickle.dump((model, vectorizer, label_encoder), f)

print("Modèle sauvegardé dans 'model_prenoms.bin' ✨✨")
