from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk import pos_tag
from res import RESOURCES_PATH
import csv
import re


def preprocess(text):
    # nltk.download('omw-1.4')
    text = text.lower()
    text_p = "".join([char for char in text if char not in string.punctuation])
    text = word_tokenize(text_p)
    stop_words = stopwords.words('english')
    filtered_words = [word for word in text if word not in stop_words and word != "p" and word != "h" and not re.search(r'\d\d\d\d\d\d\d', word)]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in filtered_words]


def get_adjectives(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "ADJ"]


def get_nouns(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "NOUN"]


def get_verbs(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "VERB"]


WORDS = ["courage", "paper", "apprehension", "sharpener"]


def initialize_dict():
    return {word: [] for word in WORDS}


def get_all_words_defs():
    defs = initialize_dict()
    defs_file = RESOURCES_PATH / "defs.csv"

    with defs_file.open() as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for word, col in zip(WORDS, row[1:]):
                defs[word].append(preprocess(col))

    return defs


def normalize(values):
    return [(float(v) - min(values)) / (max(values) - min(values)) for v in values]


def get_content_words(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "NOUN" or tag == "ADJ" or tag == "VERB" or tag == "ADV"]

