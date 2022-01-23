from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from nltk import pos_tag


def preprocess(text):
    # nltk.download('omw-1.4')
    text = text.lower()
    text_p = "".join([char for char in text if char not in string.punctuation])
    text = word_tokenize(text_p)
    stop_words = stopwords.words('english')
    filtered_words = [word for word in text if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in filtered_words]


def preprocess_with_stop(text):
    # nltk.download('omw-1.4')
    text = text.lower()
    text_p = "".join([char for char in text if char not in string.punctuation])
    text = word_tokenize(text_p)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in text]


def get_adjectives(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "ADJ"]


def get_nouns(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "NOUN"]


def get_verbs(text):
    tagged = pos_tag(text, "universal")
    return [word for word, tag in tagged if tag == "VERB"]

