def perform_operation_on_list(input_list, index):
    try:
        result = input_list[index]
        print(f"Element at index {index}: {result}")
    except IndexError:
        print(f"Index {index} is out of range for the given list")

my_list = [1, 2, 3, 4, 5]

perform_operation_on_list(my_list, 2)
perform_operation_on_list(my_list, 10)
