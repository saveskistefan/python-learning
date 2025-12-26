

while True:
    password = input('Enter a password (must contain number): ')
    if len(password) < 6:
        print('Password too short')
        continue
    if not any(char.isdigit() for char in password):
        print('Password must contain at least 1 number')
        continue

    print('Password accepted')
    break
input('Press enter to exit')