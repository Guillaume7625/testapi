import os
import openai

# Récupérer la clé API depuis les variables d'environnement
openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("La clé API OpenAI n'a pas été trouvée dans les variables d'environnement.")

try:
    # Tester l'API avec une requête simple
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Dis bonjour en français",
        max_tokens=10
    )
    
    print("Réponse de l'API :", response.choices[0].text.strip())
    print("Test réussi!")
except Exception as e:
    print("Erreur lors du test de l'API :", str(e))
