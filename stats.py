def count_book_words(book_data):
    word_count = book_data.split()
    return len(word_count)

def count_book_characters(book_data):
    book_data_list = list(book_data.lower())
    character_set = set()
    for char in book_data_list:
        character_set.add(char.lower())
    character_dict = {}
    for char in character_set:
        count = book_data_list.count(char)
        character_dict[char] = count
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_characters(character_dict):
    sorted_character_dict = []

    for char in character_dict:
        if char.isalpha():
            print(f"{char} is alphabetical")
            sorted_character_dict.append({"character": char, "count": character_dict[char]})
        
    sorted_character_dict.sort(reverse=True, key=sort_on) 

    return sorted_character_dict
