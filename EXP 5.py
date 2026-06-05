from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "jumps", "easily", "studies", "playing"]

print("Original Words -> Stemmed Words")
for word in words:
    print(word, "->", ps.stem(word))
