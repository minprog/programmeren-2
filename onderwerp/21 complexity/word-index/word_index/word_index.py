# word_index.py: Find all occurance of a word in a text.
# Usage: python word_index.py [text-file]
# Displays all line numbers where the word occrus.

import sys, string

def read_stopwords():
    """
    Read all the stopwords from the file "stopwords.txt".
    Returns the collection of stopwords.
    """
    with open("stopwords.txt") as f:
        stopwords = [s.strip() for s in f.readlines()]

    # TODO: finish

def convert_word(s):
    """
    Strips a word from all puncuation, whitespace, and digits. Then converts
    the word into all lower case.
    """
    return s.strip(string.punctuation + \
                   string.whitespace + \
                   string.digits).lower()

def create_index(filename, stopwords):
    """
    Reads `filename` and returns an index.
    * For each word in the file, the index contains a record of all line numbers where this word occurs.
    * Words are converted to lowercase and stripped of punctuation, whitespace and digits.
    * Empty strings and stopwords are not indexed.
    """

    # TODO: initialize an index for all the words.

    with open(filename, encoding = 'ISO-8859-1') as f:
        # Read the lines in the file and give them a number
        for line_number, line in enumerate(f.readlines(), 1):

            # Split the line into a list of strings (splits on spaces)
            for s in line.split():
                word = convert_word(s)

                # TODO: add word to index (ignore empty words and stopwords)

    # TODO: return the index

def search_index(word, book_index):
    """
    Find the word in book_index. Returns all the lines where word occurs.
    """
    # TODO: implement

def show_search_results(word, line_numbers):
    """
    Displays the search results (line_numbers) nicely.
    """
    # TODO: implement

def user_input_search(book_index):
    """
    User input loop. For every line provided as input, convert it, find the line
    numbers, and show results.
    """
    line = input("\nEnter search term: ")
    while line not in ["q", "Q", "quit", ""]:
        searched_word = convert_word(line)
        line_numbers = search_index(searched_word, book_index)
        show_search_results(searched_word, line_numbers)

        line = input("\nEnter search term: ")


if __name__ == "__main__":
    # Read the stopwords from the stopwords file
    stopwords = read_stopwords()

    if len(sys.argv) < 2:
        print("No arguments provided.", \
              "Please specifiy the file you want to search.")
        sys.exit()

    # Uses first command line argument as infile to build an index of words
    book_index = create_index(sys.argv[1], stopwords)

    print("Index built for", sys.argv[1]+".",
            "Type the word you want to look up.")

    # Start the user input loop
    user_input_search(book_index)
