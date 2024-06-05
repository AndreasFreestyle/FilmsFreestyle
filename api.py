import customtkinter as ctk
import webbrowser
import requests

def film():
    # Récupérer les films sur le site
    id_key = text_input.get()
    print(f"Texte entré: {id_key}")
    api_key = '195c3a3949d344fb58e20ae881573f55'
    base_url = f'https://api.themoviedb.org/3/list/{id_key}?api_key={api_key}&page='
    all_movies = []
    response = requests.get(base_url + '1')

    if response.status_code == 200:
        # Convertir la réponse en JSON
        data = response.json()
        total_pages = data['total_pages']

        all_movies.extend(data['items'])

        for page in range(2, total_pages + 1):
            response = requests.get(base_url + str(page))
            if response.status_code == 200:
                data = response.json()
                all_movies.extend(data['items'])
            else:
                print(f"Erreur : Impossible de récupérer la page {page}")
    else:
        print("Erreur : Impossible de récupérer la liste des films")

    with open('films.txt', 'w', encoding='utf-8') as file:
        for item in all_movies:
            movie_id = item.get('id', 'ID non disponible')
            file.write(f"{movie_id}\n")

    print("Les informations des films ont été écrites dans le fichier 'films.txt'")

def open_help():
    url_help = "https://raw.githubusercontent.com/AndreasFreestyle/FilmsFreestyle/main/help.png"
    webbrowser.open(url_help)


# Initialiser customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Créer la fenêtre principale
app = ctk.CTk()
app.geometry("600x400")
app.title("Mon API")

# Définir l'icône de la fenêtre
app.iconbitmap("icone.ico")

# Titre stylisé
title_text = (
    "███████╗   ███████╗\n"
    "██   ╔═╝   ██   ╔═╝\n"
    "█████║     █████║\n"
    "██╔══╝     ██╔══╝\n"
    "██║        ██║\n"
    "══╝        ══╝ "
)

# Créer le label pour le titre
title_label = ctk.CTkLabel(master=app, text=title_text, font=("Courier", 12), justify="left")
title_label.pack(pady=10)

# Créer les boutons
btn_liste_films = ctk.CTkButton(master=app, text="Mon ID de ma liste", command=film)
btn_liste_films2 = ctk.CTkButton(master=app, text="Comment trouver l'ID de sa liste ?", command=open_help)

# Créer un champ de saisie de texte
text_input = ctk.CTkEntry(master=app, placeholder_text="Entrez un ID de la liste ici")

# Ajouter les elements à la fenêtre principale
btn_liste_films.pack(pady=10)
text_input.pack(pady=20)
btn_liste_films2.pack(pady=10)

label = ctk.CTkLabel(master=app, text="Si vous avez déjà entré votre ID de votre liste, vous pouvez fermer cette page.", font=("Arial", 15))
label.pack(pady=20)

# Lancer l'application
app.mainloop()