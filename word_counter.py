import string

try:
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Error: '{file_name}' was not found.")
    exit()

print('Select what you want to do.')
print('1. get the most used word')
print('2. get the total amount of words')

selection = input("Selection: ").strip()

if selection == '1':
    word_map = {}
    most_used = ''
    maximum = 0

    for word in contents.split():
        word.strip(string.punctuation).lower()
        if word in word_map:
            word_map[word] += 1
        else: word_map[word] = 1

    for key in word_map:
        amount = word_map[key]
        if amount > maximum:
            maximum = amount
            most_used = key

    print(f"Most used word in '{file_name}': {most_used}")
    print(f"Amount of times used: {maximum}")

elif selection == '2':
    words = contents.split()
    print(f"Total amount of words: {len(words)}")

else:
    print("Invalid input. Please enter '1' or '2'.")