from res import RESOURCES_PATH
from exercises.utils import preprocess
import csv
from collections import Counter
import itertools


def initialize_dict():
    defs = {}
    defs.setdefault("courage", [])
    defs.setdefault("paper", [])
    defs.setdefault("apprehension", [])
    defs.setdefault("sharpener", [])
    return defs


def get_all_words_defs():
    defs = initialize_dict()
    defs_file = RESOURCES_PATH / "defs.csv"

    with open(defs_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            defs.get("courage").append(preprocess(row[1]))
            defs.get("paper").append(preprocess(row[2]))
            defs.get("apprehension").append(preprocess(row[3]))
            defs.get("sharpener").append(preprocess(row[4]))

    return defs


def normalize(values):
    return [(float(v) - min(values)) / (max(values) - min(values)) for v in values]


def get_words_counts(defs):
    joined = list(itertools.chain.from_iterable(defs))
    counter = Counter(joined)
    return counter


def similarity(definition, words_counts):
    # intersection = set.intersection(*defs.get(word))
    # l'intersezione tra le definizioni è nulla per cui utilizzeremo un altro criterio:
    # il punteggio di similarità  sarà dato dalla somma delle frequenze delle parole utilizzate nella definizione
    # diviso la lunghezza della definizione

    freq_sum = sum(words_counts[word] for word in definition)
    return freq_sum / len(definition)


def average_similarity(defs):
    words_counts = get_words_counts(defs)
    similarities = [similarity(d, words_counts) for d in defs]
    similarities = normalize(similarities)
    return sum(similarities) / len(similarities)


def calculate_similarities():
    results = initialize_dict()
    all_words_defs = get_all_words_defs()
    for word in ("courage", "paper", "apprehension", "sharpener"):
        single_word_defs = all_words_defs.get(word)
        results[word] = average_similarity(single_word_defs)
    return results


def print_aggregations():
    similarities = calculate_similarities()
    abstract = (similarities["courage"] + similarities["apprehension"]) / 2
    concrete = (similarities["paper"] + similarities["sharpener"]) / 2
    generic = (similarities["courage"] + similarities["paper"]) / 2
    specific = (similarities["apprehension"] + similarities["sharpener"]) / 2

    print("astratto", abstract)
    print("concreto", concrete)
    print("generico", generic)
    print("speifico", specific)


if __name__ == "__main__":
    print_aggregations()