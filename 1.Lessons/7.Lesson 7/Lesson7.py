# Input validation and simple logic
while True:
    hours = input("Enter hours worked (1-16): ").replace(',', '.')
    if hours.replace('.', '', 1).isdigit() and 1 <= float(hours) <= 16:
        hours = float(hours)
        break
    else:
        print("Invalid input. Try again.")

while True:
    quality = input("Enter quality (1-10): ")
    if quality.isdigit() and 1 <= int(quality) <= 10:
        quality = int(quality)
        break
    else:
        print("Invalid input. Try again.")

print(f"Hours: {hours}, Quality: {quality}")