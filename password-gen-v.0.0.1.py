"""
    author : Liteboho Maseli
    date   : 29/01/24
    title  : Password Generator
    version: Python 3.11.7

"""

import string
import random

UPPERCASE = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Get user input to determine length of password and password designation
designation = str(input("Where will the password be used? : "))
print("The password will be used for:", designation)

length = int(input("Enter the length of your password: "))

# Display the user input
print("You entered:", length)


def generate_password(length):
    #combine letters, digits and symbols
    characters = UPPERCASE + lowercase + digits + symbols
    
    #The password should include atleast one character from each category
    password = random.choice(UPPERCASE) + random.choice(lowercase) + random.choice(digits) + random.choice(symbols) 

    #generate remaining characters randomly
    password += ''.join(random.choice(characters) for l in range(length - len(password)))

    #shuffle the password to make it more random
    password_list = list(password)  #create list from password string
    random.shuffle(password_list)
    password = ''.join(password_list)  #join the list characters into a single string

    return password

# Example: Generate a password with default length (12 characters)
generated_password = generate_password(length)
print("Generated Password:", generated_password)

#Export the password to a file
file = open("output.txt", "a")
file.write("\n")
file.write("\n")
file.write("platform: ")
file.write(designation)
file.write("\n")
file.write("Password: ")
file.write(generated_password)
file.close()

#open and read the file after the overwriting
file = open("output.txt", "r")
print(file.read())

