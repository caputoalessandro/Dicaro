from res import RESOURCES_PATH
from exercises.utils import preprocess
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from collections import Counter


VERB = ["bless", "blessed"]
INVALID_ARGUMENTS = ["“", "p", "v", "u", "2", "3", "→", "4",
                     "5", "6", "7", "8", "9", "0", "’", "bless",
                     "blessed", "blessing", "blesses"]


def exraction_rule(word, tag):
    return word not in INVALID_ARGUMENTS and tag != "VERB" and tag != "ADV"


def get_object(tagged_words, index):
    for word, tag in tagged_words[index + 1:]:
        if exraction_rule(word, tag):
            return word


def get_subject(tagged_words, index):
    for word, tag in reversed(tagged_words[:index]):
        if exraction_rule(word, tag):
            return word


def get_arguments(line):
    tagged = pos_tag(line, "universal")
    for word, tag in tagged:
        if word in VERB:
            index = line.index(word)
            subject = get_subject(tagged, index)
            object = get_object(tagged, index)
            if subject and object:
                return [subject, object]


def get_istance(line):
    tokenized = word_tokenize(line)
    if set(VERB).intersection(tokenized):
        line = preprocess(line)
        arguments = get_arguments(line)
        if VERB[0] in tokenized:
            return arguments
        elif VERB[1] in tokenized and arguments is not None:
            return get_arguments(line).reverse()


def get_istances():
    corpus_path = RESOURCES_PATH / "blessed_corpus.txt"
    with open(corpus_path) as f:
        lines = f.readlines()
        return [get_istance(line) for line in lines if get_istance(line) is not None]


def get_semantic_type(arg):
    if wn.synsets(arg):
        st = wn.synsets(arg)[0].lexname()
        if "noun" in st:
            return st.split('.')[1]


def get_semantic_types(istances):
    return [get_semantic_type(istance[0]) for istance in istances], [get_semantic_type(istance[1]) for istance in istances]


def print_semantic_clusters(subj, obj):
    print("{:<20} {:<20}".format("Subject", "Object"))
    print("{:<20} {:<20}".format("___________", "___________"))
    for k1, k2 in zip(subj, obj):
        print("{:<20} {:<20}".format(k1, k2))


def main():
    istances = get_istances()
    subj, obj = get_semantic_types(istances)

    subj_freqs = Counter(subj)
    obj_freqs = Counter(obj)
    subj_freqs.pop(None)
    obj_freqs.pop(None)

    print_semantic_clusters(subj_freqs, obj_freqs)


if __name__ == "__main__":
    main()