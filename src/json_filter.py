import json


path = "../woerterbuch/dwdswb-headwords.json"

data = json.loads(open(path).read())

with open('../de_6_buchstaben.txt', 'r') as de:
    dictionary = set(word.strip() for word in de)

with open('../target_wordlist.txt', 'w') as l:
    for line in data:
        if len(line) == 6:
            #if line.isalpha():
            if line in dictionary:
                l.write(f'{line}\n')