# Personal info
while True:
    name = input('Enter your name: ').strip()
    
    if name == '':
        print("Invalid, try again")
    else:
        name = name.capitalize()
        break


# Subjects
while True:
    subjects = input("How many subjects do you have?: ")

    if not subjects.isdigit():
        print("Invalid, must be a positive number")
        continue

    subjects = int(subjects)

    if subjects <= 0:
        print("Must be a positive number")
    else:
        break

subject_list = []

for i in range(subjects):
    print(f"\nSubject {i+1}")
    
    name_subject = input("Enter subject name: ").capitalize()

    while True:
        grade = input("Enter grade (1-10): ")

        if not grade.isdigit():
            print("Invalid, must be a number")
            continue

        grade = int(grade)

        if grade < 1 or grade > 10:
            print("Invalid grade, must be between 1–10")
        else:
            break

    subject_list.append((name_subject, grade))


# Workout days
while True:
    days = input("How many days did you work out?: ")

    if not days.isdigit():
        print("Invalid, must be a number")
        continue

    days = int(days)

    if days <= 0:
        print("Must be a positive number")
    else:
        break

workout_list = []

for i in range(days):
    print(f"\nDay {i+1}")
    workout_name = input("Workout name: ").capitalize()

    while True:
        duration = input("How many minutes?: ")

        if not duration.isdigit():
            print("Invalid, must be a number")
            continue

        duration = int(duration)

        if duration <= 0:
            print("Duration must be positive")
        else:
            break

    workout_list.append((workout_name, duration))


# Subject calculations
grade_list = [item[1] for item in subject_list]

average = sum(grade_list) / len(grade_list)
highest = max(grade_list)
lowest = min(grade_list)

# Workout calculations
minutes = [item[1] for item in workout_list]

total_workout = sum(minutes)
average_workout = total_workout / len(minutes)
highest_workout = max(minutes)
lowest_workout = min(minutes)


# Performance rating
if average >= 9:
    performance_grade = "Excellent student"
elif average >= 7:
    performance_grade = "Good student"
else:
    performance_grade = "Needs improvement"

if average_workout >= 60:
    performance_workout = "Super active"
elif average_workout >= 30:
    performance_workout = "Active"
else:
    performance_workout = "Not active"


# PRINTING REPORT
print(f"\n{name}'s Weekly Study & Workout Report")
print("----------------------------------------")

print("\nSubjects:")
for subject, grade in subject_list:
    print(f"- {subject}: {grade}")

print(f"\nTotal subjects: {subjects}")
print(f"Average grade: {average:.2f}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")
print(f"Performance: {performance_grade}")

print("\nWorkouts:")
for workout_name, duration in workout_list:
    print(f"- {workout_name}: {duration} minutes")

print(f"\nTotal minutes: {total_workout}")
print(f"Average minutes: {average_workout:.2f}")
print(f"Longest session: {highest_workout}")
print(f"Shortest session: {lowest_workout}")
print(f"Workout rating: {performance_workout}")

input("\nPress enter to exit")