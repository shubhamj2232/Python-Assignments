def run_length_encoding(input_string):
    if not input_string:
        return ""

    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1

    encoded_string += input_string[-1] + str(count)

    return encoded_string

input_str = "wwwwaaadebbbbbw"
result = run_length_encoding(input_str)

print(result)
