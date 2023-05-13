"""Write the code that finds the longest word in the given list.
List = ["cat","dog","bird","turtle","penguen","crocodile"]"""

# Hayrunnisa Bıyıklı - 21091010143

def find_longest_word(word_list):

    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

word_list = ["cat", "dog", "bird", "turtle", "penguen", "crocodile"]

longest_word = find_longest_word(word_list)
print("Longest word:", longest_word)




