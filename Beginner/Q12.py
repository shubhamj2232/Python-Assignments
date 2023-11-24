def reverse_no(nums):
    rev_num = 0
    while nums > 0:
        last_dig = nums % 10
        rev_num = rev_num * 10 + last_dig
        nums //= 10
    return rev_num

inp = int(input("Enter a number: "))
print("Reversed Number is:", reverse_no(inp))
