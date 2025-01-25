# -*- coding: utf-8 -*-
import math
from collections import Counter

class PasswordStrengthTester:
    def __init__(self):
        self.categories = {
            'lowercase': set('abcdefghijklmnopqrstuvwxyz'),
            'uppercase': set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
            'digits': set('0123456789'),
            'special': set('!@#$%^&*()_+-=[]{}|;:,.<>?')
        }

    def calculate_entropy(self, password):
        # Calcul de l'entropie selon la formule de Shannon
        if not password:
            return 0
        
        # Calculer la taille de l'alphabet utilise
        alphabet_size = 0
        for category in self.categories.values():
            if any(char in category for char in password):
                alphabet_size += len(category)
        
        # Calculer l'entropie
        password_length = len(password)
        entropy = password_length * math.log2(alphabet_size) if alphabet_size > 0 else 0
        
        return round(entropy, 2)

    def evaluate_strength(self, password):
        entropy = self.calculate_entropy(password)
        
        # Criteres bases sur l'ANSSI
        if entropy >= 100:
            strength = "Tres fort"
        elif entropy >= 80:
            strength = "Fort"
        elif entropy >= 60:
            strength = "Moyen"
        else:
            strength = "Faible"
        
        # Verification des criteres supplementaires
        categories_used = 0
        for category in self.categories.values():
            if any(char in category for char in password):
                categories_used += 1
        
        return {
            'entropy': entropy,
            'strength': strength,
            'length': len(password),
            'categories_used': categories_used
        }