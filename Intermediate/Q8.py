def count_vowels(input_string):
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for char in input_string if char in vowels)
    return vowel_count

input_string = "Hello, World!"
vowel_count_result = count_vowels(input_string)
print("Number of vowels:", vowel_count_result)
