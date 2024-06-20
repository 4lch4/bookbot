def get_letters_count(text):
    letters = {}

    for letter in text:
        if letter.isalpha():
            letter = letter.lower()

            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    return letters


def get_word_count(text):
    return len(text.split())


def main():
    print("--- Frankenstein Report ---\n")

    with open("./books/frankenstein.txt", "r") as file:
        text = file.read()

        word_count = get_word_count(text)
        letters_count = get_letters_count(text)

        print(f"{word_count} words found in the text.\n")

        for letter, count in letters_count.items():
            print(f"The letter '{letter}' appears {count} times in the text.")


main()
