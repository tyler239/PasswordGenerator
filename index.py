import string
import random

alphabet = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%&*()^")

def generate_random_password():
    while True :

        length = int(input("Enter password length:"))

        alpha_count = int(input("How many letters in the password:"))
        digits_count = int(input("How many digits in the password:"))        
        special_count = int(input("How many special characters in the password:"))
        
        if length == sum([alpha_count,digits_count,special_count]):
           break 
        else:
           print("The lenght of the password inserted doest match with total count of the letters, digits and special characters!")
    password = []

    for i in range(alpha_count):
        password.append(random.choice(alphabet))
    
    for i in range(digits_count):
        password.append(random.choice(digits))
    
    for i in range(special_count):
        password.append(random.choice(special_characters))

    random.shuffle(password)

    print(''.join(password))
    
if __name__ == '__main__' :
    generate_random_password()
