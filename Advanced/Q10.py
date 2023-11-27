def cus_without_using_comp(N, S):
    stack = []
    walked_away = 0

    for customer in S:
        if customer not in stack:
            stack.append(customer)  
        else:
            if len(stack) > N:
                walked_away += 1 
            else:
                stack.remove(customer) 

    return walked_away

# Eg. 1
N1 = 3
S1 = "GACCBDDBAGEE"
result1 = cus_without_using_comp(N1, S1)
print("Example 1 Output:", result1)

# Eg. 2
N2 = 1
S2 = "ABCBAC"
result2 = cus_without_using_comp(N2, S2)
print("Example 2 Output:", result2)
