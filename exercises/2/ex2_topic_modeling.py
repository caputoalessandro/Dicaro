from gensim import corpora, models
import gensim
from res import RESOURCES_PATH
from pathlib import Path
import pprint
import pyLDAvis
import pyLDAvis.gensim_models
import numpy as np
import nltk
from exercises.utils import preprocess, get_content_words


def get_preprocessed_text(path):
    with open(path) as f:
        text = f.read()
        sentences = nltk.tokenize.sent_tokenize(text)
        return [get_content_words(preprocess(sentence)) for sentence in sentences]


def get_lda_model(corpus, id2word):
    return gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=3,
                                                random_state=100,
                                                update_every=1,
                                                chunksize=100,
                                                passes=10,
                                                alpha='auto',
                                                per_word_topics=True)


def print_topics(lda_model):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(lda_model.print_topics())


def make_visualization(lda_model, corpus, id2word, name):
    vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(vis, f'visualizations/LDA_{name}_visualization.html')


def get_segments(sentences, k):
    segments = np.array_split(sentences, k)
    return [[word for sentence in segment for word in sentence] for segment in segments]


def main():
    # corpus_path = Path(RESOURCES_PATH / "coca_news_corpus_test.txt")
    # corpus_path = Path(RESOURCES_PATH / "coca_news_corpus.txt")
    corpus_path = Path(RESOURCES_PATH / "corona_corpus.txt")
    prep_sentences = get_preprocessed_text(corpus_path)
    texts = get_segments(prep_sentences, 10)

    id2word = corpora.Dictionary(texts)
    corpus = [id2word.doc2bow(text) for text in texts]
    lda_model = get_lda_model(corpus, id2word)
    make_visualization(lda_model, corpus, id2word, corpus_path.name)
    print_topics(lda_model)


if __name__ == "__main__":
    main()
