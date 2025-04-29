def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = dict()
    for char in text.lower():
        if not char in characters:
            characters[char] = 0
        characters[char] += 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_character_count(char_dict):
    character_list = list()
    
    for i in char_dict.keys():
        character_list.append({"char": i, "num": char_dict[i]})
    
    character_list.sort(reverse=True, key=sort_on)

    return character_list