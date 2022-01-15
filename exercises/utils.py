import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk


def preprocess(text):
    # nltk.download('omw-1.4')
    text = text.lower()
    text_p = "".join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text_p)
    stop_words = stopwords.words('english')
    filtered_words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in filtered_words]

