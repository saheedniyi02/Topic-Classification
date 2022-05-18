import joblib
import nltk

from nltk.stem import WordNetLemmatizer

nltk.download("omw-1.4")
nltk.download("wordnet")


lemmatizer = WordNetLemmatizer()

vectorizer = joblib.load("assets/vectorizer.sav")
model = joblib.load("assets/model.sav")


def clean_text(text):
    text = text.replace("\n", "")
    text = text.split(" ")
    new_text = []
    for word in text:
        lemmatized_word = lemmatizer.lemmatize(word)
        new_text.append(lemmatized_word.lower())
    return " ".join(new_text)


def predict_topic(text):
    text = clean_text(text)
    text_vect = vectorizer.transform([text])
    topic = model.predict(text_vect)[0]
    return topic
