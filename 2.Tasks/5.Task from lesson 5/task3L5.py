names = []

while True:
    name = input("Enter a name (or 'x' to stop): ")

    if name.lower() == 'x':
        break

    names.append(name)

names.sort()

print("\nSorted names:")
for n in names:
    print("-", n)

input('Press enter to exit')