# Rolit

Version numérique du jeu de plateau Rolit, développée en Python. Jouable de 2 à 4 joueurs, avec sauvegarde de partie et menu de règles intégré.

## Fonctionnalités

- Mode 2 à 4 joueurs
- Plusieurs couleurs de pions au choix
- Sauvegarde et chargement de partie (`sauvegarde.json`)
- Règles du jeu consultables directement depuis le menu, sans quitter la partie
- Interface graphique développée avec **fltk**

## Prérequis

- Python 3

## Installation et lancement

1. Cloner le dépôt ou télécharger le projet :
   ```bash
   git clone https://github.com/moctaratji/Rolit.git
   cd Rolit
   ```
2. Lancer le jeu :

   **Windows**
   ```bash
   python Rolit.py
   ```

   **Linux / macOS**
   ```bash
   python3 Rolit.py
   ```

## Structure du projet

| Fichier | Rôle |
|---|---|
| `Rolit.py` | Programme principal |
| `fltk.py` | Bibliothèque graphique utilisée pour l'interface |
| `couleur_choice.py` | Sélection de la couleur de jeu |
| `clavier.py` | Saisie de lettres/chiffres dans l'interface |
| `sauvegarde.json` | Données de sauvegarde de partie |
| `regle_1.ppm` à `regle_8.ppm` | Images des règles du jeu, affichées dans le menu |
| `image_principale.ppm` | Interface du menu principal |
| `pions.ppm` | Images liées au nombre de joueurs |
| `oui.ppm` / `non.ppm` | Validation / annulation d'une action |
| `droite.ppm` / `gauche.ppm` | Navigation dans les menus |
| `menu.ppm` | Retour au menu principal |

## Auteur

Développé par [Moctar](https://github.com/moctaratji).
