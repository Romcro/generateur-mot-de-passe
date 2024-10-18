import tkinter as tk
from tkinter import ttk
import password_generator  # Assure-toi d'importer la logique de génération de mots de passe

# Création de la fenêtre
window = tk.Tk()
window.title("Générateur de mot de passe sécurisé")
window.geometry("500x800")
# Empêcher le redimensionnement de la fenêtre
window.resizable(False, False)  # False pour la largeur, False pour la hauteur

# Définir les couleurs personnalisées (inspirées de Bootstrap)
primary_color = "#6f42c1"  # Violette
secondary_color = "#ffffff"  # Blanche

# Configuration du style ttk
style = ttk.Style()
style.configure("TLabel", foreground=primary_color, font=("Arial", 12))
style.configure("TButton", background=primary_color, foreground=secondary_color, font=("Arial", 10))
style.map("TButton", background=[('active', primary_color)])  # Pour changer la couleur survolée

# Création d'un label ttk
label = ttk.Label(window, text="Nombre de mots de passe à générer :", style="TLabel")
label.pack(pady=10)

# Entrée pour le nombre de mots de passe
entry = ttk.Entry(window, width=30)
entry.pack(pady=10)

# Champ de texte pour afficher les mots de passe générés
passwords_text = tk.Text(window, height=8, width=40, bg=secondary_color, fg=primary_color)
passwords_text.pack(pady=10)

# Fonction pour générer et afficher les mots de passe
def generate_passwords():
    try:
        number_of_passwords = int(entry.get())  # Récupérer le nombre de mots de passe
        passwords = password_generator.generate_multiple_passwords(number_of_passwords)
        
        passwords_text.delete(1.0, tk.END)  # Effacer le champ de texte avant d'afficher les nouveaux mots de passe
        for i, password in enumerate(passwords, 1):
            passwords_text.insert(tk.END, f"Mot de passe {i}: {password}\n")
    
    except ValueError:
        passwords_text.delete(1.0, tk.END)  # Effacer le champ si une erreur se produit
        passwords_text.insert(tk.END, "Veuillez entrer un nombre valide.")

# Bouton pour générer les mots de passe
button = ttk.Button(window, text="Générer", command=generate_passwords, style="TButton")
button.pack(pady=10)

# Boucle principale Tkinter
window.mainloop()
