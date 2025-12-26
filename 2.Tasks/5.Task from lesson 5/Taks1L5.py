number_list = []

while True:
    num = input("Enter a number (or type 'stop' to finish): ")
    if num.lower() == 'stop':
        break
    else:
        num = float(num)
        number_list.append(num)

total = sum(number_list)
average = total / len(number_list)
highest = max(number_list)
lowest = min(number_list)

print(f'You entered {len(number_list)} numbers')
print(f'Total: {total}')
print(f'Average: {average:.2f}')
print(f'Highest: {highest}')
print(f'Lowest: {lowest}')

input("Press enter to exit")