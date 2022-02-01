from res import RESOURCES_PATH
from pathlib import Path
import nltk
from exercises.utils import preprocess, normalize
import numpy as np
from itertools import combinations


def get_vector(sentence, matrix):
    for word in sentence:
        if word in matrix:
            matrix[word] = matrix[word] + 1
    return np.array(list(matrix.values()))


def initialize_matrix(segment):
    return {word: 0 for sentence in segment for word in sentence}


def get_vectors(segment):
    ris = []
    for sentence in segment:
        matrix = initialize_matrix(segment)
        ris.append(get_vector(sentence, matrix))
    return ris


def get_lexical_score(segment):
    vectors = get_vectors(segment)
    return sum(x.dot(y) for x, y in combinations(vectors, 2))


def get_lexical_scores(segments):
    return [get_lexical_score(segment) for segment in segments]


def get_segmentation_score(segments):
    scores = get_lexical_scores(segments)
    return sum(normalize(scores))


def find(interval, sentences):
    for s1, s2 in interval:
        new_score = len(set(s1) & set(s2))
        if new_score == 0:
            return sentences.index(s2)
    return None


def get_stops(indexes, start):
    forward_stop = backward_stop = start
    index = indexes.index(start)

    if index != (len(indexes)-1):
        forward_stop = indexes[index + 1]

    if index != 0:
        backward_stop = indexes[index - 1] + 1

    if index == 0:
        backward_stop = 0

    return forward_stop, backward_stop


def find_breakpoint(sentences, start, prev_bp, next_bp):
    forward_interval = zip(sentences[start: next_bp], sentences[start + 1:next_bp])
    backward_interval = zip(sentences[prev_bp:start], sentences[prev_bp+1:start])
    forward_bp = find(forward_interval, sentences)
    backward_bp = find(backward_interval, sentences)

    if backward_bp and forward_bp and abs(start - forward_bp) > abs(start - backward_bp):
        return backward_bp
    elif forward_bp:
        return forward_bp
    else:
        return start


def get_bp_indexes(segments):
    bp_indexes = [(None, 0)]
    for segment in segments:
        index = len(segment) + bp_indexes[-1][1]
        bp_indexes.append((segment, index))
    bp_indexes.remove((None, 0))
    return bp_indexes


def make_pairs_indexes(sentences, bps):
    pairs = []
    pairs.append((0, bps[0]))
    for v1, v2 in zip(bps, bps[1:]):
        pairs.append((v1 + 1, v2))
    pairs.append((bps[-1] + 1, len(sentences)))
    return pairs


def update_segments(sentences, segments):
    result = []

    for i in range(len(segments)):
        segments_indexes = get_bp_indexes(segments)
        bp = segments_indexes[i][1]

        result_bps = get_bp_indexes(result)
        if i != 0:
            prev_bp = result_bps[-1][1]
        else:
            prev_bp = 0

        if i < len(segments_indexes)-1:
            next_bp = segments_indexes[i+1][1]
        else:
            next_bp = len(sentences)

        new_bp = find_breakpoint(sentences, bp, prev_bp, next_bp)
        result.append(sentences[prev_bp:new_bp])

    return result


def get_segments(sentences, k):
    segments = np.array_split(sentences, k)
    return [[sentence for sentence in segment] for segment in segments]


def get_sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    return [preprocess(sentence) for sentence in sentences]


def segmentation(text, iterations, bps):
    sentences = get_sentences(text)
    segments = get_segments(sentences, bps)
    segmentation_results = []

    for i in range(iterations):
        segments = update_segments(sentences, segments)
        segments = [segment for segment in segments if segment != []]
        segs_indexes = get_bp_indexes(segments)
        indexes = [s[1] for s in segs_indexes]
        new_score = get_segmentation_score(segments)
        segmentation_results.append((segments, new_score, indexes))

    best = max(segmentation_results, key=lambda x: x[1])
    return segmentation_results, best


def print_results(segmentation_result, best):
    for segment, score, indexes in segmentation_result:
        print(indexes, score)
    print("\nBest segments: ", best[2], best[1])
    print("______________________________________________________________")
    print("\n")


def main():
    articles_path = Path(RESOURCES_PATH / "segmentation")
    for article in articles_path.iterdir():
        with open(article) as f:
            text = f.read()
            segmentation_result, best = segmentation(text, 10, 20)
            print_results(segmentation_result, best)


if __name__ == "__main__":
    main()

