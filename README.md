
# Générateur de Mot de Passe Sécurisé

## Description
Ce projet est un générateur de mot de passe sécurisé écrit en Python. L'application permet de générer des mots de passe aléatoires en fonction de critères définis, tels que la longueur et l'utilisation de lettres, chiffres, et symboles spéciaux.

L'interface graphique a été créée en utilisant **Tkinter** pour une expérience utilisateur simple et intuitive. Ce projet est packagé sous forme d'exécutable pour macOS (format `.dmg`), disponible dans ce dépôt.

## Fonctionnalités
- Génération de mots de passe sécurisés.
- Choix du nombre de mots de passe à générer.
- Interface utilisateur simple avec **Tkinter**.
- Possibilité de personnaliser l'icône de l'application.

## Installation et Exécution

### Utilisation de l'exécutable macOS (fichier `.dmg`)
Un fichier `.dmg` est disponible dans ce dépôt pour les utilisateurs de macOS. Voici comment l'utiliser :
1. Téléchargez le fichier **`generateur_mot_de_passe.dmg`** depuis le répertoire `dist/`.
2. Double-cliquez sur le fichier `.dmg` pour monter l'image disque.
3. Faites glisser l'icône de l'application dans votre dossier **Applications**.
4. Lancez l'application depuis le dossier **Applications**.

### Utilisation sous Windows (génération de l'exécutable `.exe`)
Si vous êtes sous Windows et souhaitez générer un exécutable `.exe`, suivez les étapes suivantes :

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/ton-utilisateur/nom-du-repo.git
   cd generateur-mot-de-passe
   ```

2. **Créer un environnement virtuel et installer les dépendances** :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur macOS/Linux
   .venv\Scripts\activate      # Sur Windows

   pip install -r requirements.txt
   ```

3. **Générer l'exécutable `.exe`** avec PyInstaller :
   ```bash
   pyinstaller --onefile --windowed --icon=favicon.ico --name=generateur_de_mot_de_passe app.py
   ```

4. **Récupérer l'exécutable** :
   Une fois la commande terminée, l'exécutable **`generateur_de_mot_de_passe.exe`** sera disponible dans le dossier `dist/`.

## Prérequis
- **Python 3.x** doit être installé pour exécuter le projet ou pour créer l'exécutable.
- Les dépendances sont listées dans le fichier **`requirements.txt`** et incluent :
  - **Tkinter** (installé par défaut avec Python).
  - **PyInstaller** (si vous souhaitez créer des fichiers `.exe` ou `.dmg`).

## Contenu du dépôt
- **`app.py`** : Le fichier principal contenant la logique du générateur de mots de passe.
- **`password_generator.py`** : Le module Python qui gère la logique de génération des mots de passe.
- **`dist/`** : Contient l'exécutable `.dmg` pour macOS.
- **`favicon.ico`** : L'icône de l'application.
- **`requirements.txt`** : Les dépendances nécessaires pour exécuter le projet.
- **`.gitignore`** : Fichiers et dossiers ignorés par Git (comme `dist/`, `build/`, etc.).

## Comment contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à créer des **issues** ou à soumettre des **pull requests**. Toute aide est la bienvenue pour améliorer les fonctionnalités, corriger des bugs ou ajouter des fonctionnalités supplémentaires !

## Licence
Ce projet est sous licence MIT. Voir le fichier **LICENSE** pour plus de détails.
```
