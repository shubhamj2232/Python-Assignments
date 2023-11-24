def is_power_of_two(n):
    if n == 1:
        return True
    elif n < 1 or n % 2 != 0:
        return False
    else:
        return is_power_of_two(n // 2)

number = 16
result = is_power_of_two(number)
print(f"Sample Output: {result}")
