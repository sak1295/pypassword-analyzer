import unittest
from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

class TestPasswordTools(unittest.TestCase):
    def setUp(self):
        self.tester = PasswordStrengthTester()
        self.generator = PasswordGenerator()
        self.passphrase_gen = PassphraseGenerator()

    def test_password_strength(self):
        # Test mot de passe faible
        result = self.tester.evaluate_strength("abc123")
        self.assertLess(result['entropy'], 60)
        self.assertEqual(result['strength'], "Faible")

        # Test mot de passe fort
        result = self.tester.evaluate_strength("Abcd1234!@#$")
        self.assertGreaterEqual(result['entropy'], 80)
        self.assertIn(result['strength'], ["Fort", "Très fort"])

    def test_password_generator(self):
        password = self.generator.generate_password(8, 2, 2, 2)
        self.assertEqual(len(password), 14)  # 8 + 2 + 2 + 2
        
        # Vérifier que le mot de passe contient bien tous les types de caractères
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        self.assertTrue(all([has_lower, has_upper, has_digit, has_special]))

    def test_passphrase_generator(self):
        passphrase = self.passphrase_gen.generate_passphrase(5)
        words = passphrase.split()
        self.assertEqual(len(words), 5)

if __name__ == '__main__':
    unittest.main()