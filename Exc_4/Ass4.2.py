def unique_words(filename):
    unique_words_set = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation marks if necessary
                    word = word.strip(".,?!-:;\"'()")

                    # Add the word to the set
                    unique_words_set.add(word)

        # Display the unique words
        print("Unique words found in the file:")
        for word in unique_words_set:
            print(word)

    except FileNotFoundError:
        print("File not found.")

# Example usage: provide the filename as an argument
filename = "text.txt"
unique_words(filename)
