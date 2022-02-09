from collections import Counter
import itertools
from exercises.utils import get_nouns, get_adjectives, get_all_words_defs, WORDS, initialize_dict, normalize


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
        mfw = list(mfw)
        adj_noun = get_nouns(mfw) + get_adjectives(mfw)
        result.append((word, adj_noun))

    return result


def print_results(similarities, aggregations, explanation):

    print("|Concept|Similarity|")
    print("|  ---  |  ---  |")
    for word, similarity in similarities.items():
        print(f'|{word}|{similarity:.2f}|')

    print("\n")

    print("|Aggregation|Similarity|")
    print("|  ---  |  ---  |")
    for aggregation, mean_similarity in aggregations:
        print(f'|{aggregation}|{mean_similarity:.2f}|')

    print("\n")

    print("|Concept| Most frequent words|")
    print("|  ---  |  ---  |")
    for word, frequent_words in explanation:
        print(f'|{word}| {frequent_words}|')


def main():
    similarities = get_similarities()
    aggregations = get_aggregations(similarities)
    explanation = get_similarty_explanation()
    print_results(similarities, aggregations, explanation)


if __name__ == "__main__":
    main()

