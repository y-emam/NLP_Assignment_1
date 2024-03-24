# Importing Libraries:
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re


def preprocess_text(text):
    # convert text to lowercases
    text = text.lower()

    # Remove HTML tages
    text = re.sub("<[^<]+?>", "", text)

    # Remove Special characters and digits
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Tokenizartion
    tokens = word_tokenize(text)

    # Remove Stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatizer_token = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatizer_token


def get_unique_words(url):
    # Fetch HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Get the text in the page
    text = soup.get_text()
    print("text:\n", text, "\n")

    # Preprocess text
    preprocessed_text = preprocess_text(text)

    # Get unique words
    unique_words = set(preprocessed_text)

    ans = []
    for word in unique_words:
        if word.length() < 3:
            ans.append(word)

    return unique_words


url = "https://www.quora.com/How-can-I-extract-website-content-with-natural-language-processing"
unique_words = get_unique_words(url)
print(unique_words)
