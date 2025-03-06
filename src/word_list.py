class WordList:
    def __init__(self):
        with open('../target_wordlist.txt', 'r') as f:
            self.solution = 'TRABEN'
        with open('../wordlist.txt', 'r') as w:
            self.dictionary = set(word.strip().upper() for word in w)

    def get_dictionary(self):
        return self.dictionary

    def get_solution(self):
        return self.solution