#Curtis Lincoln
#Challenge 22

Word_1 = input("Type in a word: ")
Word_2 = input("Type in another word: ")

if sorted(Word_1.lower()) == sorted(Word_2.lower()):
    print("The two words are anagrams of each other.")

else:
    print("These two words are not anagrams of each other.")
