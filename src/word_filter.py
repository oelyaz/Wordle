import codecs

with codecs.open('../woerterbuch/german.dic', 'r', encoding='iso-8859-1') as f:
    for line in f:
        if len(line) == 8:
            with open('../de_6_buchstaben.txt', 'a') as de:
                de.write(line)

source_path = '../woerterbuch/uni_leipzig/deu_wikipedia_2021_1M/deu_wikipedia_2021_1M-words.txt'

with codecs.open('../woerterbuch/2000_german_firstnames.txt', 'r', encoding='iso-8859-1') as n:
    first_names = set(word.strip() for word in n)

with open('../de_6_buchstaben.txt', 'r') as de:
    dictionary = set(word.strip() for word in de)


with open(source_path, 'r', encoding='utf-8') as s:
    filtered = []
    for line in s:
        word = line.split('\t')[1]
        filtered.append(word) if word in dictionary and word not in first_names else word

with open('../wordlist.txt', 'w') as l:
    l.write('\n'.join(filtered))

with open('../woerterbuch/cpos/cpos_wortliste.txt', 'r') as c:
    with open('../target_words.txt', 'w') as t:
        for line in c:
            t.write(line) if line[:6] in dictionary and len(line) == 8 else line
