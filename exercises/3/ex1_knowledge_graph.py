from py2neo import Graph, Node, Relationship
from nltk.corpus import brown
from exercises.utils import preprocess, get_content_words
import nltk
import json
import subprocess
import os.path


def get_sents_for_categories():
    return {category: brown.words(categories=category) for category in brown.categories()}


def initialize_dict():
    return {category: None for category in brown.categories()}


def save_data_in_json():
    if not os.path.isfile('brown_nodes.json'):
        data = get_words_for_categories()
        with open('brown_nodes.json', 'w') as fp:
            json.dump(data, fp)
    else:
        print("File esistente")


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
        result[category] = fdist.most_common()
    return result


def create_graph(category_to_words, to_keep):
    g = Graph("neo4j://localhost:7687", auth=("neo4j", "test"))
    g.delete_all()
    USED_IN = Relationship.type("USED_IN")

    for category, words in category_to_words.items():
        category_node = Node("Category", lemma=category)
        for word, freq in words[:to_keep]:
            if not g.nodes.match("Word", lemma=word):
                word_node = Node("Word", lemma=word)
            else:
                word_node = g.nodes.match("Word", lemma=word).first()
            g.merge(USED_IN(word_node, category_node, freq=freq), "Word", "lemma")


def main():
    subprocess.Popen(['bash', '-c', '. docker.sh; run_docker'])
    save_data_in_json()
    categories_for_words = get_words_for_categories_from_json()
    create_graph(categories_for_words, 50)


if __name__ == "__main__":
    main()

