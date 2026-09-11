
import random
import string

# ask the user for the length of the password and if they want any special character, numbers, etc
# basically the user decides how strong the password is

def generate_password(minimum_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters 
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    password = ""
    meet_criteria = False 
    has_number = False
    has_special = False

    while not meet_criteria or len(password) < minimum_length:
        new_character = random.choice(characters)
        password += new_character

        if new_character in digits:
            has_number = True
        elif new_character in special_chars:
            has_special = True 

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return password 


min_length = int(input("Enter minimum length: "))
has_num = input("Do you want to have numbers? (y/n): ").lower() == 'y' # if input anything else than y, it will not include a number
has_special = input("Do you want to have special characters? (y/n): ").lower() == 'y'

print("Generated password: " + generate_password(min_length, has_num, has_special))