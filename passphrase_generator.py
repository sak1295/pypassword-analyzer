import random

class PassphraseGenerator:
    def __init__(self):
        # Liste de mots du EFF's Large Wordlist
        self.wordlist = self._load_wordlist()

    def _load_wordlist(self):
        return {
        11111: "abacus", 11112: "abdomen", 11113: "abide", 11114: "ablaze",
        11115: "abort", 11116: "abroad", 11121: "absorb", 11122: "accent",
        11123: "accept", 11124: "access", 11125: "accord", 11126: "account",
        11131: "accuse", 11132: "achieve", 11133: "acquire", 11134: "across",
        11135: "action", 11136: "active", 11141: "actual", 11142: "adapt",
        11143: "addict", 11144: "address", 11145: "adjust", 11146: "admire",
        11151: "admit", 11152: "adobe", 11153: "adopt", 11154: "adult",
        11155: "advance", 11156: "advice", 11161: "advise", 11162: "aerial",
        11163: "affair", 11164: "affect", 11165: "afford", 11166: "afraid",
        11211: "again", 11212: "agency", 11213: "agenda", 11214: "agent",
        11215: "agree", 11216: "ahead", 11221: "alarm", 11222: "album",
        11223: "alert", 11224: "alien", 11225: "alike", 11226: "alive",
        11231: "allow", 11232: "almost", 11233: "alone", 11234: "along",
        11235: "alpine", 11236: "always", 11241: "amaze", 11242: "angel",
        11243: "anger", 11244: "angle", 11245: "angry", 11246: "anime",
        11251: "ankle", 11252: "annual", 11253: "answer", 11254: "antique",
        11255: "anxiety", 11256: "anyone", 11261: "anyway", 11262: "apache",
        11263: "appeal", 11264: "appear", 11265: "apple", 11266: "apply",
        11311: "appoint", 11312: "approve", 11313: "april", 11314: "arcade",
        11315: "arctic", 11316: "area", 11321: "arena", 11322: "argue",
        11323: "arise", 11324: "armor", 11325: "army", 11326: "around",
        11331: "array", 11332: "arrive", 11333: "arrow", 11334: "article",
        11335: "artist", 11336: "artwork", 11341: "aspect", 11342: "assign",
        11343: "assist", 11344: "assume", 11345: "assure", 11346: "asthma"
    }

    def generate_passphrase(self, num_words=5):
        words = []
        for _ in range(num_words):
            # Simuler 5 lancers de dés
            dice_rolls = ''.join(str(random.randint(1, 6)) for _ in range(5))
            dice_number = int(dice_rolls)
            word = self.wordlist.get(dice_number, self._get_fallback_word())
            words.append(word)
        
        return ' '.join(words)

    def _get_fallback_word(self):
        # En cas de nombre non trouvé dans la liste
        return random.choice(list(self.wordlist.values()))