import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The boys are playing games and running quickly."
words = text.split()

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Header
print(f"{'Word':<15}{'Stem':<15}{'Lemma':<15}")
print("-" * 45)

# Data
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:<15}{stem:<15}{lemma:<15}")
