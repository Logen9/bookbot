
def get_character_map_for_whole_text(text: str):
    results = {}
    for character in text.lower():
        if character in results:
            results[character] += 1
        else:
             results[character] = 1
    return results

def sort_on(dict):
    return dict["num"]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    book = "books/frankenstein.txt"
    total_words_counter = 0

    book_text = get_book_text(book)
    
    total_words_counter += len(book_text.split())
    freq_dict = get_character_map_for_whole_text(book_text)
    
    list_of_dicts = []
    for char, count in freq_dict.items():
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(f'Total number of words: {total_words_counter}')

    print('Characters frequencies')
    for item in list_of_dicts:
        print(f'Character: {item["char"]}, detected: {item["num"]} times')

if __name__ == "__main__":
    main()