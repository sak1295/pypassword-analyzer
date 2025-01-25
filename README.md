# README.md
# Générateur et Testeur de Mots de Passe

Un outil de sécurité pour générer et tester des mots de passe, respectant les recommandations de l'ANSSI.

## Fonctionnalités

1. Testeur de mot de passe
   - Calcul de l'entropie
   - Évaluation de la force selon les critères ANSSI
   - Analyse des catégories de caractères utilisées

2. Générateur de mot de passe
   - Génération personnalisable (minuscules, majuscules, chiffres, caractères spéciaux)
   - Évaluation automatique du mot de passe généré

3. Générateur de passphrase
   - Utilisation de la méthode des dés
   - Liste de mots EFF
   - Évaluation de la force de la passphrase

## Installation

Aucune dépendance externe n'est requise

## Utilisation

Pour lancer le programme :
```bash
python main.py
```

Pour les tests unitaires :
```bash
python -m unittest test_password_tools.py
```

## Structure du projet

- `password_strength.py` : Classe pour tester la force des mots de passe
- `password_generator.py` : Classe pour générer des mots de passe aléatoires
- `passphrase_generator.py` : Classe pour générer des passphrases
- `main.py` : Interface utilisateur
- `test_password_tools.py` : Tests unitaires