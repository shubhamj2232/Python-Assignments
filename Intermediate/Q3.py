def count_pairs_with_sum(arr, k):
    element_frequency = {}
    pair_count = 0

    for num in arr:
        complement = k - num
        if complement in element_frequency:
            pair_count += element_frequency[complement]
        element_frequency[num] = element_frequency.get(num, 0) + 1
    return pair_count

arr = [1, 2, 3, 4, 5]
k = 6

result = count_pairs_with_sum(arr, k)
print("Sample Output: Pair count:", result)
