class PluralFSM:
    def generate_plural(self, noun):
        

        if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return noun + "es"
        

        elif noun.endswith('y') and noun[-2].lower() not in "aeiou":
            return noun[:-1] + "ies"
        
        else:
            return noun + "s"


fsm = PluralFSM()

nouns = ["cat", "dog", "bus", "box", "church", "baby", "city"]

print("Singular\tPlural")
print("-" * 25)

for noun in nouns:
    print(f"{noun:<10}\t{fsm.generate_plural(noun)}")
