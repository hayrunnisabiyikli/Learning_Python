def count_word_frequency(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        # Read the file contents
        contents = file.read()

        # Split the contents into words
        words = contents.split()

        # Count the frequency of each word
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def display_word_frequency(word_freq):
    # Display the frequency of each word
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")


def save_word_frequency(word_freq, output_file):
    with open(output_file, 'w') as file:
        # Write the word frequencies to the output file
        for word, frequency in word_freq.items():
            file.write(f"{word}: {frequency}\n")


# Main program
input_file = 'text.txt'
output_file = 'word_frequencies.txt'

word_freq = count_word_frequency(input_file)

# Display the word frequencies
display_word_frequency(word_freq)

# Save the word frequencies to a file
save_word_frequency(word_freq, output_file)
