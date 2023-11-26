def en_string(encoded_string):
    parts = encoded_string.split('0')

    parts = [part for part in parts if part]

    result_dict = {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

    return result_dict

# Eg.
encoded_string = "Robert000Smith000123"
result = en_string(encoded_string)

#Result
print(result)
