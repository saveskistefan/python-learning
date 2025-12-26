number = int(input('Give me a number and i will give you all even numbers till yours: '))
for num in range(1,number+1):
    if num %2 == 0:
        print(num)

input('Press enter to exit')