# README.md
# G�n�rateur et Testeur de Mots de Passe

Un outil de s�curit� pour g�n�rer et tester des mots de passe, respectant les recommandations de l'ANSSI.

## Fonctionnalit�s

1. Testeur de mot de passe
   - Calcul de l'entropie
   - �valuation de la force selon les crit�res ANSSI
   - Analyse des cat�gories de caract�res utilis�es

2. G�n�rateur de mot de passe
   - G�n�ration personnalisable (minuscules, majuscules, chiffres, caract�res sp�ciaux)
   - �valuation automatique du mot de passe g�n�r�

3. G�n�rateur de passphrase
   - Utilisation de la m�thode des d�s
   - Liste de mots EFF
   - �valuation de la force de la passphrase

## Installation

Aucune d�pendance externe n'est requise

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
- `password_generator.py` : Classe pour g�n�rer des mots de passe al�atoires
- `passphrase_generator.py` : Classe pour g�n�rer des passphrases
- `main.py` : Interface utilisateur
- `test_password_tools.py` : Tests unitaires