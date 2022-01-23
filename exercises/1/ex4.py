from res import RESOURCES_PATH
from exercises.utils import preprocess
from nltk import pos_tag
from nltk import word_tokenize


VERB_FORMS = ["bless", "blessed", "blessing", "blesses"]
VERB = ["bless", "blessed"]
TRASH = ["“", "p", "v", "u", "2", "3", "→", "4", "5", "6", "7", "8", "9", "0", "’"]


def exraction_rule(word, tag):
    return word not in VERB_FORMS and word not in TRASH and tag != "VERB" and tag != "ADV"


def get_second_argument(tagged_words, index):
    for word, tag in tagged_words[index + 1:]:
        if exraction_rule(word, tag):
            return word


def get_first_argument(tagged_words, index):
    for word, tag in reversed(tagged_words[:index]):
        if exraction_rule(word, tag):
            return word


def get_neighbors_verb(line):
    tagged = pos_tag(line, "universal")
    for word, tag in tagged:
        if word in VERB:
            index = line.index(word)
            second_argument = get_first_argument(tagged, index)
            first_argument = get_second_argument(tagged, index)
            if first_argument and second_argument:
                return [first_argument, second_argument]


def get_istance(line):
    tokenized = word_tokenize(line)
    if VERB[0] in tokenized or VERB[1] in tokenized:
        line = preprocess(line)
        return get_neighbors_verb(line)


def get_istances():
    corpus_path = RESOURCES_PATH / "blessed_corpus.txt"
    with open(corpus_path) as f:
        lines = f.readlines()
        return [get_istance(line) for line in lines if get_istance(line) is not None]


def main():
    istances = get_istances()
    print()


if __name__ == "__main__":
    main()