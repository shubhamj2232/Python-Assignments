def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

num = int(input("Enter a number: "))
if perfect_number(num):
    print("Yes")
else:
    print("No")