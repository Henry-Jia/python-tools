'''
Markov Chain.
Trains from an initial text to generate similar strings.
'''
import random
import string

def generate(text, key_len=2):
    training = {}
    key = []

    for word in text.replace("\n", " ").split():
        if len(key) == key_len:
            key_str = " ".join(key)
            try:
                training[key_str] += [word]
            except KeyError:
                training[key_str] = [word]
            key.pop(0)
        if "." in word:
            key = []
            continue
        key += [word]

    return training

def structure(training_set, start, length):
    chain = start.split()
    key_len = len(chain)-1

    for x in range(1, length):
        try:
            key = " ".join(chain[x-key_len:x+1])
            chain.append(random.choice(training_set[key]))
        except KeyError:
            break

    return chain

if __name__ == "__main__":

    source = open("sample/christmascarol.txt", "r").read()
    dictionary = generate(source, 2)

    initial_phrase = random.choice(list(dictionary.keys()))
    markov = structure(dictionary, initial_phrase, 20)
    print(" ".join(markov))
