def reverse_words(sentence):
    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

inp_sentence = "Hello, World! Welcome to Python programming."
out_sentence = reverse_words(inp_sentence)

print("Input sentence:", inp_sentence)
print("Output after reverse:", out_sentence)
