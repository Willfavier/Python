```python
import random

def choisir_phrase_depuis_fichier(fichier):
    """Charge et choisit une citation aléatoire depuis un fichier."""
    with open(fichier, 'r', encoding='utf-8') as f:
        phrases = f.readlines()
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]
    return random.choice(phrases)
