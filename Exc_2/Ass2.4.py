def count_occurrences_of_the(text):
    """This function takes a text input and finds and displays the occurrences of the word "the" in the text."""
# Hayrunnisa Bıyıklı - 21091010143
    text = text.lower()
    words = text.split(" ")
    count = 0

    for word in words:
        if word == "the":
            count += 1
    print(f"The word 'the' occurs {count} times in the given text.")

text = '''The Wretched of the Earth (French: Les Damnés de la Terre) is a 1961 
book by the philosopher Frantz Fanon, in which the author provides a
psychoanalysis of the dehumanizing effects of colonization upon the 
individual and the nation, and discusses the broader social, cultural, 
and political implications of establishing a social movement for the 
decolonization of a person and of a people. The French-language title 
derives from the opening lyrics of "The Internationale".'''

count_occurrences_of_the(text)






