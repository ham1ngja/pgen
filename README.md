# pgen.py

Pgen.py is a program that creates a cryptographically insecure password. It was designed for learning purposes only, and it should not be used for real-world applications.

Below, you will find the entire source code for the program. A breakdown is available [further down](#code-explanation) if you wish to learn more about how it works line by line.

```python
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
```

## Code Explanation

### User Input

The first function that we encounter is `user_input()`, whose purpose is to obtain arguments through `argparse`.

```python
password_special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'
```

The very first line of the function declares a variable and assigns a string to it. This string is a list of symbols that can be used in passwords. This will be used to construct the password later on.

```python
parser = argparse.ArgumentParser(description='Generate a likely insecure password.')
```

This sets up the argument parser.

#### Arguments

```python
parser.add_argument('--length', type=int, required=True, help='An integer representing the length of the password.')
```

The code above adds the first argument, `--length`. When used in the program, this argument allows the user to specify the length of the password. The `type=int` specifies that the input should be an integer, and the `required=True` portion means that a value is required for the program to run.

```python
parser.add_argument('-s', action='store_true', help='Include special characters in the password.')
```

The `-s` argument enables the use of symbols in the password. The list used is contained in the `password_special_characters` variable initialized earlier.

The `action='store_true`' allows us to store a Boolean value, either True or False, which tells the program whether the argument has been invoked.

```python
parser.add_argument('-n', action='store_true', help='Include numbers in the password.')
parser.add_argument('-u', action='store_true', help='Include uppercase letters in the password.')
parser.add_argument('-l', action='store_true', help='Include lowercase letters in the password.')
```

The code above adds the `-n`, `-u`, and `-l` arguments. These activate the use of numbers, uppercase, and lowercase letters respectively.

#### Output

```python
output_group = parser.add_mutually_exclusive_group(required=True)
```

The code above allows us to add a mutually exclusive group. This consists of several arguments, of which only one can be selected.

```python
output_group.add_argument('-t', action='store_true', help='Output the password to the command line.')
```

The `-t` argument, stored as a Boolean, enables the user to output the generated password to the terminal.

```python
output_group.add_argument('-c', action='store_true', help='Output the password to the clipboard.')
```

If you wish to output directly to the keyboard, you may use the `-c` argument.

```python
output_group.add_argument('-f', type=str, metavar='PATH', help='Output the password to a file.')
```

Alternatively, if you wish to output to a file, you may use the `-f` argument, followed by a path.

### Parsing

```python
args = parser.parse_args()
```

This parses the arguments provided by the user.

### Argument Extraction

```python
length = args.length
include_special = args.s
include_numbers = args.n
include_upper = args.u
include_lower = args.l
output_terminal = args.t
output_clipboard = args.c
output_file = args.f
```

The code above extracts the arguments provided and places each in a variable. Depending on the variable, the values are integer, boolean, or string.

### Character List

```python
possible_characters = ''
```

First, we initialize the `possible_characters` variable. Based on the user's arguments, we add character sets to it, from which the password is generated.

```python
if include_special:
	possible_characters += password_special_characters
```

If `include_special` is true, then we append the special characters mentioned earlier to the possible list of characters.

```python
if include_numbers:
	possible_characters += string.digits
```

If the user uses the `-n` argument, and thus `include_numbers` is true, digits from 0 to 9 will be added to the possible list of characters.

```python
if include_upper:
	possible_characters += string.ascii_uppercase
```

If upper-case characters are selected, they will be added to the possible list of characters.

```python
if include_lower:
	possible_characters += string.ascii_lowercase
```

Finally, if the `-l` argument is provided, all lowercase letters from the English alphabet will be added to the possible list.

### Character Check

```python
if not possible_characters:
	print("Error: No character types selected. Please select at least one character type (-s, -n, -u, -l).")
	exit(1)
```

Before we continue, we must ensure that at least one argument apart from `--length` was included. If `possible_characters` is empty, an error message is printed, and the program is stopped.

### Function Call

```python
length, possible_characters, output_terminal, output_clipboard, output_file = user_input()
```

This initial function is called from the main block. The `user_input()` function returns `length`, `possible_characters`, `output_terminal`, `output_clipboard`, and `output_file`. The code above allots those values to local variables.

## Generate Password

Once the input is obtained and parsed, and the total list of possible characters is assembled, the `generate_passwrd(length, possible_characters)` function is called from the main block.

```python
password = ''.join(random.choice(possible_characters) for _ in range(length))
```

The code above takes a random character from the possible list of characters and appends it to a `password`. This happens `n` number of times, where `n` is the length of the password. The function then returns the generated password.

## Output

The final function call made from the main block is `output_password(password, output_terminal, output_clipboard, output_file)`. This passes along the password and the three variables indicating the selected output form.

They are mutually exclusive, so two of them will be `False`, and one will be `True`. To determine which is `True`, multiple `if` statements are used.

```python
if output_terminal:
    print(password)
```

The first `if` statement determines if `output_terminal` is `True`. If it is, then it prints the password to the terminal.

```python
elif output_clipboard:
    pyperclip.copy(password)
```

The next snippet of code determines if `output_clipboard` is `True`. If it is, it uses `pyperclip` to copy the password to the clipboard.

```python
elif output_file:
	try:
		with open(output_file, 'w') as file:
			file.write(password)
		print(f"The password has been written to {output_file}.")
	except Exception as e:
		print(f"Error writing to file: {e}")
```

Finally, the third option prints to a file. First, we `try` to open the file, and write the password to it. If successful, we output that to the terminal, along with the name of the file.

However, if we are unsuccessful for various reasons, an error message is printed instead.

## Quality Assurance

Let us test the code for bugs and any potential user input that might break the program.

### Length Only

**Input**
```bash
python3 pgen.py --length 25
```

**Output**
```
usage: pgen.py [-h] --length LENGTH [-s] [-n] [-u] [-l] (-t | -c | -f PATH)
pgen.py: error: one of the arguments -t -c -f is required
```

As expected, if only the length is provided as an argument, this results in an error.

### Length and Output Only

**Input**
```bash
python3 pgen.py --length 25 -t
```

**Output**
```
Error: No character types selected. Please select at least one character type (-s, -n, -u, -l).
```

If only the length and output type are provided, this also results in an error, as expected.

### No Length

**Input**
```bash
python3 pgen.py -t
```

**Output**
```
usage: pgen.py [-h] --length LENGTH [-s] [-n] [-u] [-l] (-t | -c | -f PATH)
pgen.py: error: the following arguments are required: --length
```

When no length is provided, an error occurs, as expected.

### No Output

**Input**
```bash
python3 pgen.py --length 25 -snul
```

**Output**
```
usage: pgen.py [-h] --length LENGTH [-s] [-n] [-u] [-l] (-t | -c | -f PATH)
pgen.py: error: one of the arguments -t -c -f is required
```

When no output is provided, an error occurs.

### Only Length and -s

**Input**
```bash
python3 pgen.py --length 25 -s -t
```

**Output**
```
%^_<_!^;;&$>\_[/#+\;@>}$^
```

When only the `-s` argument type is provided, the password is made up of special characters only.

### Only Length and -n

**Input**
```bash
python3 pgen.py --length 25 -n -t
```

**Output**
```
7297523397587354727818692
```

When only `-n` is selected, the output is numbers only.

### Only Length and -u

**Input**
```bash
python3 pgen.py --length 25 -u -t
```

**Output**
```
WPLRYHTKRDVJTNTQLQQVGKXVP
```

If only `-u` is provided, then the password is all uppercase letters.

### Only Length and -l

**Input**
```bash
python3 pgen.py --length 25 -l -t
```

**Output**
```
vncspaclamlhtwmwqelzncfho
```

When only `-l` is provided, the output is lowercase only.

### Full -t Output

**Input**
```bash
python3 pgen.py --length 25 -snul -t
```

**Output**
```
Kw#E{[E*5w}]JH$m4-j$aHA^f
```

When all arguments are present, and `-t` is used for output, the password is printed to the terminal.

### Full -c Output

**Input**
```bash
python3 pgen.py --length 25 -snul -c
```

**Output**
```
```

When the `-c` argument is provided, nothing is output to the terminal, and the password is copied to the clipboard instead.

### Full -f Output

**Input**
```bash
python3 pgen.py --length 25 -snul -f output.txt
```

**Output**
```
The password has been written to output.txt.
```

If the `-f` argument is provided by the user, with the path as `output.txt`, the password is saved to the file.

```bash
cat output.txt
```

When the above command is executed, this is the output:

```
5dwjP*MpVV99&w\h$[CREm$Sb
```

### Full -f Output With Existing File

**Input**
```bash
python3 pgen.py --length 25 -snul -f output.txt
```

**Output**
```
The password has been written to output.txt.
```

If `output.txt` already exists, it will overwrite the initial file with the new password.
