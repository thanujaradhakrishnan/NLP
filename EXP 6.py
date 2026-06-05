import random
from nltk import bigrams

text = "I study natural language processing and I study python"

words = text.split()

bigram_list = list(bigrams(words))

model = {}

for w1, w2 in bigram_list:
    if w1 not in model:
        model[w1] = []
    model[w1].append(w2)

current_word = "I"
generated_text = [current_word]

for i in range(10):
    if current_word in model:
        next_word = random.choice(model[current_word])
        generated_text.append(next_word)
        current_word = next_word
    else:
        break

print("Generated Text:")
print(" ".join(generated_text))
