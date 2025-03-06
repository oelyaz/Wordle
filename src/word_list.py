import random


class WordList:
    def __init__(self):
        with open('../assets/target_wordlist.txt', 'r') as f:
            words = f.readlines()
            self.solution = random.choice(words).strip().upper()

        with open('../assets/wordlist.txt', 'r') as w:
            self.dictionary = set(word.strip().upper() for word in w)

    def get_dictionary(self):
        return self.dictionary

    def get_solution(self):
        return self.solution