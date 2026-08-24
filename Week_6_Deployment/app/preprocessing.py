"""
NLP Preprocessing Module for Spam Classifier
5-step text cleaning pipeline
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


def preprocess_text(text):
    """
    5-step NLP preprocessing pipeline
    """
    # 1. Lowercasing
    text = text.lower()
    
    # 2. Tokenization
    tokens = word_tokenize(text)
    
    # 3. Special Character Removal
    tokens = [token for token in tokens if token.isalnum()]
    
    # 4. Stopword & Punctuation Removal
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # 5. Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return ' '.join(tokens)
