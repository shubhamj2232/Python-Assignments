def count_freq(input_list):
    freq_dict = {}

    for element in input_list:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    return freq_dict

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

result = count_freq(input_list)
print("Element frequencies:")
for element, count in result.items():
    print(f"{element}: {count}")
