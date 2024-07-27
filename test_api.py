import os
import openai

# Configurer la clé API
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Faire une requête à l'API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Vous êtes un assistant utile."},
            {"role": "user", "content": "Bonjour, comment allez-vous ?"}
        ]
    )
    
    # Afficher la réponse
    print("Réponse de l'API :")
    print(response.choices[0].message['content'])
    print("\nTest réussi!")
except Exception as e:
    print(f"Erreur lors du test de l'API : {str(e)}")
