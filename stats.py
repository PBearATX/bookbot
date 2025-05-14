def count_words(string: str) -> int:
    word_count = len(string.split())
    return word_count


def count_characters(string: str) -> dict[str, int]:
    character_count = {}
    for ch in string:
        lower_ch = ch.lower()
        if lower_ch in character_count:
            character_count[lower_ch] += 1
        else:
            character_count[lower_ch] = 1

    return character_count


def sort_character_count(character_count: dict[str, int]):
    ch_list = []
    for ch, count in character_count.items():
        entry = dict(char=ch, num=count)
        ch_list.append(entry)

    ch_list.sort(reverse=True, key=lambda x: x["num"])
    return ch_list
