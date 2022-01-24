from nltk.corpus import wordnet as wn
from exercises.utils import WORDS, get_all_words_defs, preprocess
from collections import Counter

# 1. prendere tutte le definizioni di un concetto dell'es.1
# 2. usare il meccanismo "genus": prendo le parole più frequenti delle definizioni
# 3. immaginare che  quelle parole possano essere i genus, e cercarle su wn
# 4. andiamo a vedere gli iponimi di quei synset  e  vediamo quali tra le gloss matchano meglio.


def have_hyponyms(word):
    synsets = wn.synsets(word)
    return synsets and synsets[0].hyponyms()


def get_score(hyponym,defs):
    hyp_def = preprocess(hyponym.definition())
    intersection = set(defs) & set(hyp_def)
    return len(intersection)


def get_similarity(concept, defs):
    synset = wn.synsets(concept)[0]
    scores = [(hyponym, get_score(hyponym, defs)) for hyponym in synset.hyponyms()]
    return max(scores, key=lambda x: x[0])[0]


def get_form(defs):
    defs = [w for d in defs for w in d]
    hypernyms_freq = Counter(defs).most_common()
    hypernyms = [t[0] for t in hypernyms_freq if have_hyponyms(t[0])][:10]
    similarities = [(hypernym, get_similarity(hypernym, defs)) for hypernym in hypernyms]
    return max(similarities, key=lambda x: x[0])[0]


def get_forms():
    words_defs = get_all_words_defs()
    return [get_form(words_defs[word]) for word in WORDS]


def main():
    print(get_forms())


if __name__ == "__main__":
    main()
