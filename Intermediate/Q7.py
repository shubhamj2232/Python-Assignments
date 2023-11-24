def find_median(number_list):
    if not number_list:
        return "List is empty"
    sorted_list = sorted(number_list)

    n = len(sorted_list)
    if n % 2 == 0:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        median = sorted_list[n // 2]

    return f"Median: {median}"

number_list = [7, 2, 5, 1, 9, 3]

median_result = find_median(number_list)
print("Sample Output:", median_result)
