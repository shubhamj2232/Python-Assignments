def no_divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Consultadd - Python Training"
    elif n % 3 == 0:
        return "Consultadd"
    elif n % 5 == 0:
        return "Python Training"
    else:
        return "No suitable training found"

n = int(input("Enter a number: "))
print(no_divisible(n))