def count_let_and_dig(str1):
    letter_count = 0
    digit_count = 0

    for char in str1:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    return letter_count, digit_count

# Input from user
str1 = input("Enter a string: ")

letters, digits = count_let_and_dig(str1)

print("Alphabets:", letters, "& Number :", digits)