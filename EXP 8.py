import random

pos_probabilities = {
    "dog": ["NN"],
    "cat": ["NN"],
    "runs": ["VB"],
    "eats": ["VB"],
    "quickly": ["RB"],
    "happy": ["JJ"]
}

sentence = "dog runs quickly"

words = sentence.split()

tagged_sentence = []

for word in words:
    if word in pos_probabilities:
        tag = random.choice(pos_probabilities[word])
    else:
        tag = "NN"  # default tag
    tagged_sentence.append((word, tag))

print("Tagged Sentence:")
print(tagged_sentence)
