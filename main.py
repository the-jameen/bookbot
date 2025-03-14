import sys
from stats import *

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
book_path = sys.argv[1]

def get_book_text(bookpath):

    with open(bookpath) as f:
        book_contents = f.read()
    return(book_contents)

def main():
    book_content = get_book_text(book_path)

    book_word_count = count_book_words(book_content)

    book_character_count = count_book_characters(book_content)

    character_sort = sort_characters(book_character_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for char in character_sort:
        print(f"{char["character"]}: {char["count"]}")
    print("============= END ===============")

    sys.exit(0)


main()