def word_reverse():
    word = input("Enter the word: ")
    new_word = ""
    for i in reversed(word):
            new_word += i

    print(f"{new_word}")

word_reverse()