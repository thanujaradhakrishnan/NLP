import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "The cat is sitting on the mat."

words = word_tokenize(text)

tagged = pos_tag(words)

print("POS Tags:")
print(tagged)
