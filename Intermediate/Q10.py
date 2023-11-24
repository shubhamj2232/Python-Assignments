def stone_piles(n):
    is_even = n % 2 == 0
    piles = []

    for i in range(2, n, 2):
        piles.append(i)
    return piles

n = 7
stone_piles_result = stone_piles(n)
print("Stones in a single pile =", stone_piles_result)
