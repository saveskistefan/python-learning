

while True:
    name = input('Tell me your name: ')
    if name == '':
        print('Invalid name')
    else:
        name = name.capitalize()
        break


while True:
    subject = input('How many subject you have?: ')
    if not subject.isdigit():
        print('Invalid,Must be a number')
        continue
    subject = int(subject)

    if subject <= 0:
        print('Must be a positive number')
    else:
        break
subject_list = []
for i in range(subject):
    print(f'Subject{i+1}')
    name_subject = input('Subject name: ')
    
    while True:
        grade = int(input('Tell me your grade'))
        if grade <= 0:
            print('Invalid grade(must be between 1-10)')
            continue
        elif grade > 10:
            print('Invalid grade(must be between 1-10)')
            continue
        else:
            break
    subject_list.append((name_subject,grade))
        
grade_list = [item[1] for item in subject_list]

total_subjects = subject
average = sum(grade_list) / len(grade_list)
highest = max(grade_list)
lowest = min(grade_list)

print(f'{name} grade report:\n----------')

for name_subject,grade in subject_list:
    print(f'-{name_subject}: {grade}')

print(f'Total subjects: {total_subjects}')
print(f'Average: {average}')
print(f'Highest: {highest}')
print(f'Lowest: {lowest}')

input('Press enter to exit')


