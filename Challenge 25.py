#Curtis Lincoln
#Challenge 25
import string

Sentence = input("Type in a sentence: ").lower()
Sentence = Sentence.translate(str.maketrans('','', string.punctuation))

if Sentence[::-1] == Sentence:
    print("This sentence is a palindrome")
else:
    print("This sentence is not a palidrome")





