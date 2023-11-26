with open("Advanced\doc.txt", "r") as file:
    content = file.read()
words = content.split()

even_length_words = [word for word in words if len(word) % 2 == 0]

result = ' '.join(even_length_words)
print(result)
