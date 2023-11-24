def com_elements(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    com_elements_set = set1.intersection(set2)
    com_elements_list = list(com_elements_set)
    return com_elements_list

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

result = com_elements(l1, l2)
print("Common Elements are:", result)
