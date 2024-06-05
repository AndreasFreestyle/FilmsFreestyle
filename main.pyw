import subprocess
import webbrowser
import customtkinter as ctk
from choisir_film import choisir_film

# Initialiser customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Créer la fenêtre principale
app = ctk.CTk()
app.geometry("600x400")
app.title("FilmsFreestyle")

# Définir l'icône de la fenêtre
app.iconbitmap("icone.ico")

def github():
    webbrowser.open("https://github.com/AndreasFreestyle/FilmsFreestyle")
def yt():
    webbrowser.open("https://www.youtube.com/channel/UCZiBjVFiVs41PV5JqnxMocQ")
# Titre stylisé
title_text = (
    "███████╗   ███████╗\n"
    "██   ╔═╝   ██   ╔═╝\n"
    "█████║     █████║\n"
    "██╔══╝     ██╔══╝\n"
    "██║        ██║\n"
    "══╝        ══╝ "
)


def open_other_script():
    subprocess.run(["python", "api.py"])

# Créer le label pour le titre
title_label = ctk.CTkLabel(master=app, text=title_text, font=("Courier", 12), justify="left")
title_label.pack(pady=10)

# Créer les boutons
btn_liste_films = ctk.CTkButton(master=app, text="Liste de films", command=open_other_script)
btn_choisir_film = ctk.CTkButton(master=app, text="Choisir un film", command=choisir_film)
btn_github = ctk.CTkButton(master=app, text="le GitHub",width=100, height=25 , command=github)
btn_yt = ctk.CTkButton(master=app, text="la chaine YouTube",width=100, height=25 , command=yt)

# Ajouter les boutons à la fenêtre principale
btn_liste_films.pack(pady=10)
btn_choisir_film.pack(pady=10)
btn_github.pack(pady=10)
btn_yt.pack(pady=10)

# Lancer l'application
app.mainloop()