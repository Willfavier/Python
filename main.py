import tkinter as tk
from tkinter import messagebox
from .utils import choisir_phrase_depuis_fichier

def afficher_citation():
    fichier_phrases = "data/Liste_citation_motivation.txt"
    try:
        citation = choisir_phrase_depuis_fichier(fichier_phrases)
        citation_label.config(text=citation)
        citation_label.config(foreground="#ffffff")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

fenetre = tk.Tk()
fenetre.title("Citation Motivante")
fenetre.geometry("600x400")
fenetre.resizable(False, False)
fenetre.config(bg="#111111")

font_btn = ("Helvetica", 14, "bold")
font_label = ("Helvetica", 16, "italic")

container = tk.Frame(fenetre, bg="#111111", padx=20, pady=20)
container.pack(expand=True, fill=tk.BOTH)

titre_label = tk.Label(container, text="Citation Motivante", font=("Helvetica", 26, "bold"), bg="#111111", fg="#FF6F61")
titre_label.pack(pady=20)

choisir_fichier_btn = tk.Button(container, text="Afficher une citation", command=afficher_citation, font=font_btn, bg="#FF6F61", fg="white", relief="flat", padx=20, pady=10)
choisir_fichier_btn.pack(pady=30)

citation_label = tk.Label(container, text="", font=font_label, bg="#111111", fg="#FFFFFF", wraplength=500, justify="center")
citation_label.pack(pady=20)

fenetre.mainloop()
