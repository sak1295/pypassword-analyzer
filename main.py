# -*- coding: utf-8 -*-
from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

def main():
    tester = PasswordStrengthTester()
    generator = PasswordGenerator()
    passphrase_gen = PassphraseGenerator()

    while True:
        print("\nGestionnaire de Mots de Passe")
        print("1. Tester un mot de passe")
        print("2. Generer un mot de passe")
        print("3. Generer une passphrase")
        print("4. Quitter")
        
        choice = input("\nChoisissez une option (1-4): ")
        
        if choice == '1':
            password = input("Entrez le mot de passe a tester: ")
            result = tester.evaluate_strength(password)
            print(f"\nResultats:")
            print(f"Entropie: {result['entropy']} bits")
            print(f"Force: {result['strength']}")
            print(f"Longueur: {result['length']} caracteres")
            print(f"Categories utilisees: {result['categories_used']}/4")
            
        elif choice == '2':
            try:
                lower = int(input("Nombre de minuscules (defaut 8): ") or "8")
                upper = int(input("Nombre de majuscules (defaut 2): ") or "2")
                digits = int(input("Nombre de chiffres (defaut 2): ") or "2")
                special = int(input("Nombre de caracteres speciaux (defaut 2): ") or "2")
                
                password = generator.generate_password(lower, upper, digits, special)
                result = tester.evaluate_strength(password)
                
                print(f"\nMot de passe genere: {password}")
                print(f"Entropie: {result['entropy']} bits")
                print(f"Force: {result['strength']}")
                
            except ValueError:
                print("Erreur: Veuillez entrer des nombres valides.")
                
        elif choice == '3':
            try:
                num_words = int(input("Nombre de mots (defaut 5): ") or "5")
                passphrase = passphrase_gen.generate_passphrase(num_words)
                print(f"\nPassphrase generee: {passphrase}")
                
                # Evaluer la force de la passphrase
                result = tester.evaluate_strength(passphrase.replace(" ", ""))
                print(f"Entropie: {result['entropy']} bits")
                print(f"Force: {result['strength']}")
                
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide.")
                
        elif choice == '4':
            print("Au revoir!")
            break
            
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 4.")

if __name__ == "__main__":
    main()