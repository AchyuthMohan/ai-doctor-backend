import nltk
import numpy as np

# nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence.lower())

def stem(word):
    return nltk.PorterStemmer().stem(word.lower())


def bag_of_words(tokenized_sentence , all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag


# a = " How is my health?"
# print(tokenize(a))

b = ["How", "is", "my", "health"]

words = ["orgnize","organization","organizing"]
stemmed_words = [stem(w) for w in words]
# print(stemmed_words)

