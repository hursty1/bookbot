from stats import get_word_count, get_character_count
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(f'./{sys.argv[1]}')
    
    count = get_word_count(book)

    chars = get_character_count(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for k,v in chars.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")


main()