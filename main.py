import sys
from stats import count_words, count_characters, sort_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents


def pretty_print_ch_list(ch_list: list[dict[str, str | int]]):
    for ch_stat in ch_list:
        if ch_stat["char"].isalpha():
            print(f'{ch_stat["char"]}: {ch_stat["num"]}')


def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_character_count = sort_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    pretty_print_ch_list(sorted_character_count)
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    main()
