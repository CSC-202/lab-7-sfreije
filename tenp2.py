from typing import List
import string
f= open('sample_text','w')
m= open('stop_file','w')
f.write('This is a sample data ((text)) file, to be processed by your word-concordance program!!! A REAL data files is MUCH bigger. Gr8!')
m.write("a about be by can do i in is it of on the this to was ")

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def hash(self, key):
        n = min(len(key), 8)
        hash_value = 0
        for i in range(n):
            hash_value += ord(key[i]) * (31 ** (n - 1 - i))
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash(key)
        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size
        if self.table[index] is None:
            self.count += 1
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

    def resize(self):
        self.size *= 2
        new_table = [None] * self.size
        for item in self.table:
            if item is not None:
                index = self.hash(item[0])
                while new_table[index] is not None:
                    index = (index + 1) % self.size
                new_table[index] = item
        self.table = new_table


def make_hash(size: int) -> HashTable:
    return HashTable(size)


def hash_size(ht: HashTable) -> int:
    return ht.size


def hash_count(ht: HashTable) -> int:
    return ht.count


def has_key(ht: HashTable, word: str) -> bool:
    return ht.get(word) is not None


def lookup(ht: HashTable, word: str) -> List[int]:
    value = ht.get(word)
    return [] if value is None else value


def add(ht: HashTable, word: str, line: int) -> None:
    value = ht.get(word)
    if value is None:
        ht.insert(word, [line])
    elif line not in value:
        value.append(line)


def hash_keys(ht: HashTable) -> List[str]:
    keys = []
    for item in ht.table:
        if item is not None:
            keys.append(item[0])
    return keys


def make_concordance(stop_words_file: str, text_file: str) -> HashTable:
    stop_words = []
    m = open(stop_words_file).read()
    print(m)
    for line in m:
        stop_words.extend(line.strip().split())

    concordance_ht = HashTable(191)
    line_number = 1

    f= open(text_file).read()
    for line in f:
        print(line)
        line = line.replace("'", "")
        line = line.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
        tokens = line.split()
        for token in tokens:
            if token.isalpha() and token.lower() not in stop_words:
                word = token.lower()
                print(token)
                add(concordance_ht, word, line_number)
        line_number += 1
        load_factor = hash_count(concordance_ht) / hash_size(concordance_ht)
        if load_factor > 0.5:
            concordance_ht.resize()

    return concordance_ht

def generate_concordance_file(concordance):
    with open('without_punctuation', 'w') as f:
        words= concordance.table
        print(concordance.table)
        for word in words:
            if word is not None:
                print(word)
                line_numbers = ' '.join(str(line) for line in concordance.get(word))
                f.write(f"{word}: {line_numbers}\n")

stop_words_file = "stop_file"
text_file = "sample_text"

 

concordance = make_concordance(m, f)

generate_concordance_file(concordance)

# Output: ['sample', 'data', 'text', 'file', 'processed', 'word', 'concordance', 'program', 'real', 'bigger', 'gr8']



 

print(lookup(concordance, 'file'))

# Output: [1, 3]

 

print(hash_count(concordance))

# Output: 11

 
