def sum_of_digits(n):
    sum_dig = 0
    while n > 0:
        sum_dig += n % 10
        n //=10
    return sum_dig

def red_to_single_digit(num):
    while num >= 10:
        num = sum_of_digits(num)
    return num

input_no = int(input("Enter number: "))
initial_sum = sum_of_digits(input_no)
final_no = red_to_single_digit(initial_sum)
print("The sum of digits is:",final_no ) 