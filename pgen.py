import argparse
import random
import string

import pyperclip


# Request input from the user
def user_input():
    
    # Define a set of special characters which are commonly allowed in passwords
    password_special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a likely insecure password.')
    parser.add_argument('--length', type=int, required=True, help='An integer representing the length of the password.')
    parser.add_argument('-s', action='store_true', help='Include special characters in the password.')
    parser.add_argument('-n', action='store_true', help='Include numbers in the password.')
    parser.add_argument('-u', action='store_true', help='Include uppercase letters in the password.')
    parser.add_argument('-l', action='store_true', help='Include lowercase letters in the password.')

     # Mutually exclusive group for output options
    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument('-t', action='store_true', help='Output the password to the command line.')
    output_group.add_argument('-c', action='store_true', help='Output the password to the clipboard.')
    output_group.add_argument('-f', type=str, metavar='PATH', help='Output the password to a file.')

    # Parse arguments
    args = parser.parse_args()

    # Extract arguments
    length = args.length
    include_special = args.s
    include_numbers = args.n
    include_upper = args.u
    include_lower = args.l
    output_terminal = args.t
    output_clipboard = args.c
    output_file = args.f

    # Initialize the possible characters set variable
    possible_characters = ''

    # Append appropriate character sets based on user input
    if include_special:
        possible_characters += password_special_characters

    if include_numbers:
        possible_characters += string.digits

    if include_upper:
        possible_characters += string.ascii_uppercase

    if include_lower:
        possible_characters += string.ascii_lowercase

    # Check if we have at least one type of character to create a password
    if not possible_characters:
        print("Error: No character types selected. Please select at least one character type (-s, -n, -u, -l).")
        exit(1)

    return length, possible_characters, output_terminal, output_clipboard, output_file 


def generate_password(length, possible_characters):
    # Generate a random password based on the possible characters set
    password = ''.join(random.choice(possible_characters) for _ in range(length))

    return password

def output_password(password, output_terminal, output_clipboard, output_file):
    # Handle the output based on the user's choice
    if output_terminal:
        print(password)
    elif output_clipboard:
        pyperclip.copy(password)
    elif output_file:
        try:
            with open(output_file, 'w') as file:
                file.write(password)
            print(f"The password has been written to {output_file}.")
        except Exception as e:
            print(f"Error writing to file: {e}")

# Get the returned value from user_input() and allocate them to variables, in order
length, possible_characters, output_terminal, output_clipboard, output_file = user_input()

# Generate the password
password = generate_password(length, possible_characters)

# Output the password based on user choice
output_password(password, output_terminal, output_clipboard, output_file)
