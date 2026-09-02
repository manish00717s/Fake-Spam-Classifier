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

# Build these once at import time instead of rebuilding on every call.
_STOP_WORDS = set(stopwords.words('english'))
_STEMMER = PorterStemmer()


def preprocess_text(text):
    """
    5-step NLP preprocessing pipeline.

    Steps: lowercase -> tokenize -> keep alphanumeric ->
    remove stopwords -> stem.

    Args:
        text: The raw message text. Non-string / empty input returns "".

    Returns:
        A cleaned, space-joined string of processed tokens.
    """
    # Guard against None, NaN floats, or other non-string input.
    if not isinstance(text, str) or not text.strip():
        return ""

    # 1. Lowercasing
    text = text.lower()

    # 2. Tokenization
    tokens = word_tokenize(text)

    # 3. Special Character Removal
    tokens = [token for token in tokens if token.isalnum()]

    # 4. Stopword & Punctuation Removal
    tokens = [token for token in tokens if token not in _STOP_WORDS]

    # 5. Stemming
    tokens = [_STEMMER.stem(token) for token in tokens]

    return ' '.join(tokens)
