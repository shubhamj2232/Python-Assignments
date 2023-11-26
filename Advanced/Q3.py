def JtoI(file_path):
    try:
        with open("Advanced/words.txt", 'r') as file:
            content = file.read()

        corrected_content = content.replace('J', 'I')

        print(corrected_content)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

JtoI("Advanced/words.txt")
