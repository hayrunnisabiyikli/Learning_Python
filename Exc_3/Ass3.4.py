sentence = input("Enter a sentence: ")

words = sentence.split()

pig_latin_words = []
for word in words:
    word = word.upper()
    pig_latin_word = word[1:] + word[0] + "AY"
    pig_latin_words.append(pig_latin_word)

pig_latin_sentence = " ".join(pig_latin_words)

print(pig_latin_sentence)






