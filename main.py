import string

letter_count = {letter: 0 for letter in string.ascii_lowercase}

def main(book_title):
    with open(f"books/{book_title}.txt") as f:
        print(f"--- Begin report of books/ {book_title}.txt ---")
        file_contents = f.read()
        file_contents_lower = file_contents.lower()
        list_of_words = file_contents_lower.split()
        number_of_words = (len(list_of_words))
        print(f"{number_of_words} words found in the document\n")
        for word in list_of_words:
            for letter in word:
                if letter in letter_count:
                    letter_count[letter] += 1
        sorted_letter_count = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
        for letter, count in sorted_letter_count:
            if count > 0:
                print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

main(book_title="frankenstein")