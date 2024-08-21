def digits_and_letters():
    string = input("Enter a string: ")

    digits = 0
    letters = 0
    for i in string:
        if i.isdigit():
            digits += 1 
        elif i.isalpha():
            letters += 1
    
    print(f"Number of letters: {letters}")
    print(f"Number of digits: {digits}")

digits_and_letters()