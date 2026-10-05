word1 = input("Enter word1: ")
word2 = input("Enter word2: ")

if sorted(word1) == sorted(word2):
    print("Word1 and Word2 are Anagram")
else:
    print("Word1 and Word2 are Not Anagram")