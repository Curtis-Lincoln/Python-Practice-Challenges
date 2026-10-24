#Curtis Lincoln
#Challenge 24

import string

Sentence_1 = input("Type in a sentence: ").lower()
Sentence_2 = input("Type in another sentence: ").lower()

Sentence_1 = Sentence_1.translate(str.maketrans('','', string.punctuation))
Sentence_2 = Sentence_2.translate(str.maketrans('','', string.punctuation))

if sorted(Sentence_1) == sorted(Sentence_2):
    print("The two sentences are anagrams of each other.")

else:
    print("These two sentences are not anagrams of each other.")
    




