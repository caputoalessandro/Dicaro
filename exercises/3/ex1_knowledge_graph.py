from py2neo import Graph, Node, Relationship
from nltk.corpus import brown
from exercises.utils import preprocess, get_content_words
import nltk
import json


def get_sents_for_categories():
    return {category: brown.words(categories=category) for category in brown.categories()}


def initialize_dict():
    return {category: None for category in brown.categories()}


def save_in_json(data):
    with open('brown_nodes.json', 'w') as fp:
        json.dump(data, fp)


def get_words_for_categories_from_json():
    with open('brown_nodes.json', 'r') as fp:
        return json.load(fp)


def get_words_for_categories():
    result = initialize_dict()
    s4c = get_sents_for_categories()
    for category, words in s4c.items():
        prep_words = preprocess(" ".join(list(words)))
        content_words = get_content_words(prep_words)
        fdist = nltk.FreqDist(w for w in content_words)
        result[category] = fdist.most_common(50)
        # result[category].append(tuple(fdist.items()))
    return result


def create_graph(category_to_words):
    g = Graph("neo4j://localhost:7687", auth=("neo4j", "test"))
    g.delete_all()
    USED_IN = Relationship.type("USED_IN")

    for category, words in category_to_words.items():
        category_node = Node("Category", lemma=category)
        for word, freq in words:
            if not g.nodes.match("Word", lemma=word):
                word_node = Node("Word", lemma=word)
            else:
                word_node = g.nodes.match("Word", lemma=word).first()
            g.merge(USED_IN(word_node, category_node, freq=freq), "Word", "lemma")


toy_nodes = {
    "action": [("a", 10)],
    "horror": [("b", 20), ("a", 30)]
}


def main():
    # data = get_words_for_categories()
    # save_in_json(data)
    categories_for_words = get_words_for_categories_from_json()
    create_graph(categories_for_words)


if __name__ == "__main__":
    main()