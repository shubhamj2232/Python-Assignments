def unique_elements(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = unique_elements(list1)
print("Output: list2 =", list2)
