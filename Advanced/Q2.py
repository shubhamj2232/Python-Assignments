with open("Advanced/demo.txt", "r") as file:
    line_count = sum(1 for line in file)

# Display the result
print(f"Number of lines are: {line_count}")
