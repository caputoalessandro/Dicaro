import nltk
from res import RESOURCES_PATH
import csv
from collections import Counter
import itertools
from exercises.utils import preprocess

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


def get_words_counts(defs):
    return Counter(itertools.chain.from_iterable(defs))


def similarity(definition, words_counts):
    freq_sum = sum(words_counts[word] for word in definition)
    return freq_sum / len(definition)


def average_similarity(defs):
    words_counts = get_words_counts(defs)
    similarities = [similarity(d, words_counts) for d in defs]
    similarities = normalize(similarities)
    return sum(similarities) / len(similarities)


def get_similarities():
    results = initialize_dict()
    all_words_defs = get_all_words_defs()

    for word in WORDS:
        single_word_defs = all_words_defs.get(word)
        results[word] = average_similarity(single_word_defs)

    return results


def get_aggregations(similarities ):
    result = []

    aggregations = [
        ("abstract", "courage", "apprehension"),
        ("concrete", "paper", "sharpener"),
        ("generic", "courage", "paper"),
        ("specific", "apprehension", "sharpener")
    ]

    for aggregation in aggregations:
        mean_similarity = (similarities[aggregation[1]] + similarities[aggregation[2]]) / 2
        result.append((aggregation[0], mean_similarity))

    return result


def get_similarty_explanation():
    # Prende le prime 10 parole più frequenti e restituisce solo i nomi e gli aggettivi
    all_words_defs = get_all_words_defs()
    result = []

    for word in WORDS:
        single_word_defs = all_words_defs.get(word)
        words_counts = get_words_counts(single_word_defs)
        mfw = dict(words_counts.most_common(10)).keys()
        tagged = nltk.pos_tag(list(mfw))
        adj_noun = [word for word, tag in tagged if tag == "NN" or tag == "JJ"]
        result.append((word, adj_noun))

    return result


def print_results(similarities, aggregations, explanation):

    print("------ SIMILARITIES ------")
    for word, similarity in similarities.items():
        print(word, similarity)

    print("\n")

    print("------ AGGREGATIONS ------")
    for aggregation, mean_similarity in aggregations:
        print(aggregation, mean_similarity)

    print("\n")

    print("------ MOST FREQUENT WORDS ------")
    for word, frequent_words in explanation:
        print(word, frequent_words)


def main():
    similarities = get_similarities()
    aggregations = get_aggregations(similarities)
    explanation = get_similarty_explanation()
    print_results(similarities, aggregations, explanation)


if __name__ == "__main__":
    main()

