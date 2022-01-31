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


def get_sentences(text):
    sentences = nltk.tokenize.sent_tokenize(text)
    return [preprocess(sentence) for sentence in sentences]


def find(interval, sentences):
    for s1, s2 in interval:
        new_score = len(set(s1) & set(s2))
        if new_score == 0:
            return sentences.index(s1)
    return 1000


def find_breakpoint(sentences, start):
    forward_interval = zip(sentences[start:], sentences[start + 1:])
    backword_interval = zip(sentences[:start], sentences[1:start])
    forward_bp = find(forward_interval, sentences)
    backword_bp = find(backword_interval, sentences)
    if abs(start - forward_bp) > abs(start - backword_bp):
        return backword_bp
    else:
        return forward_bp


def get_bp_indexes(segments):
    bp_indexes = [(None, 0)]
    for segment in segments:
        print()
        index = len(segment) - 1 + bp_indexes[-1][1]
        bp_indexes.append((segment, index))
    bp_indexes.remove((None, 0))
    return bp_indexes


def update_breakpoints(segments, sentences):
    segments_indexes = get_bp_indexes(segments)
    res = [find_breakpoint(sentences, index) for segment, index in segments_indexes]
    res.insert(0, 0)
    res.append(len(sentences))
    return res


def update_segments(sentences, segments):
    new_bps = update_breakpoints(segments, sentences)
    result = segments[new_bps[0]:new_bps[1]]
    for start, stop in zip(new_bps[1:], new_bps[2:]):
        result.append(sentences[start+1:stop])
    return result


def get_segments(sentences, k):
    segments = np.array_split(sentences, k)
    return [[sentence for sentence in segment] for segment in segments]


def segmentation(text, iterations):
    sentences = get_sentences(text)
    segments = get_segments(sentences, 10)

    segmentation_results = []

    for i in range(iterations):
        segments = update_segments(sentences, segments)
        new_score = get_segmentation_score(segments)
        segmentation_results.append((segments, new_score))

    best = max(segmentation_results, key=lambda x: x[1])
    return best


def main():
    articles_path = Path(RESOURCES_PATH / "segmentation")
    for article in articles_path.iterdir():
        with open(article) as f:
            text = f.read()
            segments, score = segmentation(text, 10)
            print(segments, score)


if __name__ == "__main__":
    main()

