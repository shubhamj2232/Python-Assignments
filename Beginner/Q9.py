def count_freq(input_list):
    frequency_dict = {}

    for element in input_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

result = count_freq(input_list)
print("Element frequencies:")
for element, count in result.items():
    print(f"{element}: {count}")
