start = int(input("Enter Start Number: "))
stop = int(input("End stop number: "))

sum = 0

current_no = start
while current_no <= stop:
    if current_no % 2 != 0:
        sum += current_no
    current_no += 1

print("Sum of odd numbers is:",sum)