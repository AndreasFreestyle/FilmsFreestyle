import requests
import random
import webbrowser
from api import text_input

def choisir_film():
    # Ouvrir le fichier en mode lecture
    with open('films.txt', 'r') as f:
        lines = f.readlines()

    # Choisir une ligne aléatoire
    random_line = random.choice(lines)

    # Supprimer la ligne aléatoire de la liste
    lines.remove(random_line)

    # Réécrire le contenu du fichier sans la ligne sélectionnée
    with open('films.txt', 'w') as f:
        f.writelines(lines)
    
    url = f'https://www.themoviedb.org/movie/{random_line}'
    webbrowser.open(url)

    print("La ligne suivante a été supprimée du fichier:")
    print(url)

    