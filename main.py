def main():
    path = "books/frankenstein.txt"
    text = get_books_content(path)

    print(f"Hi! Here is your report on {path}.")
    print("---------------------------------")

    print(f"There are {get_num_of_words(text)} words in the document.")
    print()

    print("Character statistics:")
    char_statistics = get_num_of_each_char(text)
    for char in char_statistics:
        print(f"'{char}' was found {char_statistics[char]} times.")

    print("---------------------------------")

def get_books_content(path_to_book):
    with open(path_to_book) as file:
        return file.read()

def get_num_of_words(text):
    words = text.split()
    return len(words)

def get_num_of_each_char(text):
    char_nums = {}
    lowercased_text = text.lower()
    for char in lowercased_text:
        if char.isalpha():
            if not char in char_nums:
                char_nums[char] = 0
            char_nums[char]  += 1
    return dict(sorted(char_nums.items()))

main()