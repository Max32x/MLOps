from flask import Flask, request, jsonify
import pickle

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle, le vectorizer et l'encodeur
with open("model_prenoms.bin", "rb") as f:
    model, vectorizer, label_encoder = pickle.load(f)

@app.route('/')
def index():
    # Page d'accueil de l'API
    return '''
    <h1>Bienvenue sur l'API de Prédiction de Genre 🐾✨</h1>
    <p>Utilisez <code>/gender?name=VotrePrenom</code> pour prédire le genre d'un prénom.</p>
    <p>Exemple : <a href="/gender?name=Christophe">/gender?name=Christophe</a></p>
    '''

@app.route('/gender', methods=['GET'])
def predict_gender():
    # Récupérer le prénom de la requête
    name = request.args.get('name', '').strip()
    if not name:
        return jsonify({"error": "Veuillez fournir un prénom via le paramètre 'name'"}), 400

    # Transformer le prénom et prédire le genre
    name_vect = vectorizer.transform([name])
    prediction = model.predict(name_vect)

    # Mapper 1 -> 'M' et 2 -> 'F'
    gender_encoded = prediction[0]
    gender = 'F' if gender_encoded == 1 else 'M'

    # Retourner la réponse JSON
    return jsonify({"name": name, "gender": gender}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

