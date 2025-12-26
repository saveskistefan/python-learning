

while True:
    email = input('Tell me your email: ')
    if "@" not in email:
        print('It must contain @')
        continue
    if '.' not in email:
        print('It must contain .')
    else:
        print('Valid email')
        break
while True:
    password = input('Enter a password: ')
    has_letter = any(ch.isalpha() for ch in password)      # True if at least one letter
    has_digit = any(ch.isdigit() for ch in password)       # True if at least one number
    has_special = any(ch in "@#$" for ch in password)
    if len(password) < 6:
        print("Password too short")
    elif not has_letter:
        print("Must contain at least one letter")
    elif not has_digit:
        print("Must contain at least one number")
    elif not has_special:
        print("Must contain at least one special symbol (@, #, $)")
    else:
        print("Password is valid")
        break
print(f'Registartion succesfull')
print(f'Your email: {email} \nYour password: {password}')

input('Press enter to exit')
    


