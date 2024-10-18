import string
import random

# Fonction pour générer un seul mot de passe
def generate_password():
    caractere = list(string.ascii_letters + string.digits + '#@&"($`=:;)')
    random.shuffle(caractere)
    password = []
    for i in range(16):  # Taille du mot de passe, ici 16 caractères
        password.append(random.choice(caractere))
    random.shuffle(password)
    return "".join(password)

# Fonction pour générer plusieurs mots de passe
def generate_multiple_passwords(number_of_passwords):
    passwords = []  # Liste pour stocker les mots de passe
    for _ in range(number_of_passwords):
        passwords.append(generate_password())
    return passwords

# Exemple : générer 5 mots de passe
number_of_passwords_to_generate = 25
passwords_list = generate_multiple_passwords(number_of_passwords_to_generate)

# Afficher chaque mot de passe généré
for i, password in enumerate(passwords_list, 1):
    print(f"Mot de passe {i} : {password}")
