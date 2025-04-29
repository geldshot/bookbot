import sys
from stats import get_word_count, get_character_count, sort_character_count

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main(path):

    print("============ BOOKBOT ============")
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    print("Analyzing book found at {path}")

    print("----------- Word Count ----------")
    character_count = get_character_count(book_text)
    print(f'Found {word_count} total words')

    print("--------- Character Count -------")
    character_list = sort_character_count(character_count)
    for i in character_list:
        print(f'{i["char"]}: {i["num"]}')

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])