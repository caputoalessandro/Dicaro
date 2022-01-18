from res import RESOURCES_PATH
import pandas as pd
from lesk import lesk
from exercises.utils import preprocess
import nltk
from nltk.corpus import wordnet as wn


# 1 cerca concetto preso da property  norm su wordnet
# 2 prendere i  synset
# 3 utilizzare le informazioni  offerte dalle property norms per scegliere il synset giusto
# quindi wsd utilizzando quello già imlementato con radicioni
# 4 trovato il synset, leghiamo il synset all'informazione,  ovvero facciamo  un match tra le feature
# chhe troviamo nelle property norm e quelle he troviamo nella definizione di wn, in più diciamo
# quali delle feature nelle porperty  norm potrebbero essere aggiunte

norms_path = RESOURCES_PATH / "norms.dat"


def convert_to_concept_feature_dict(df):
    cf_dict = {}
    for concept, feature in df["data"]:
        cf_dict.setdefault(concept, [])
        cf_dict[concept].append(feature)
    return cf_dict


def get_concepts_features():
    data = pd.read_csv(norms_path, sep='\t')
    concepts_features_df = data[["concept", "feature"]]
    splitted_dict = concepts_features_df.to_dict("split")
    return convert_to_concept_feature_dict(splitted_dict)


def tokenize_features(features):
    res = []
    for feature in features:
        for word in feature.split():
            if "_" in word:
                splitted = word.split("_")
                res.extend(splitted)
            else:
                res.append(word)
    return res


def get_adjectives(text):
    tagged = nltk.pos_tag(text)
    return [word for word, tag in tagged if tag == "JJ"]


def get_nouns(text):
    tagged = nltk.pos_tag(text)
    return [word for word, tag in tagged if tag == "NN"]


def get_features_from_wn_def(sense):
    definition = preprocess(sense.definition())
    wn_features_adj = get_adjectives(definition)
    wn_features_nouns = get_nouns(definition)
    return wn_features_adj + wn_features_nouns


def find_best_sense(concept, features):
    pn_features = tokenize_features(features)
    return lesk(concept, pn_features)


def connect_resources(cf_dict):
    mapping = {}

    for concept, pn_features in cf_dict.items():

        if not wn.synsets(concept):
            continue

        best_sense = find_best_sense(concept, pn_features)

        wn_features = get_features_from_wn_def(best_sense)
        pn_features = get_adjectives(pn_features)

        to_add = set(pn_features) - set(wn_features)

        mapping[concept] = {"wn_features": wn_features,
                            "new_features": list(to_add)[:3]}

    return mapping


def main():
    cf_dict = get_concepts_features()
    mapping = connect_resources(cf_dict)
    print(mapping)


if __name__ == "__main__":
    main()

