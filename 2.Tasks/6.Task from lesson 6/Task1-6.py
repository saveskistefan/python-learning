
#Smart focus analyzer

def tracker():
    while True:
        name = input('Tell me your name: ').strip()

        if name == '':
            print('cannot be empty')
        else:
            name = name.capitalize()
            break

    while True:
        days = input('How many days you track(1-7): ')
        if days.isdigit() and 1 <= int(days) <= 7:
            days = int(days)
            break
        else:
            print('Must be a number from 1-7')

    track_list = []
    for i in range(days):
        while True:
            focus_hours = input(f'Day {i+1}: focus hours: ')
            if focus_hours.isdigit() and int(focus_hours) >= 0:
                focus_hours = int(focus_hours)
                break
            else:
                print("Must be a positive number")

        while True:
            distractions_counts = input(f'Day {i+1}:How many distractions: ')
            if distractions_counts.isdigit() and int(distractions_counts) >= 0:
                distractions_counts = int(distractions_counts)
                break
            else:
                ('Must be a postive number')

        track_list.append((focus_hours,distractions_counts))

    return name,track_list

while True:
    name,track_list = tracker()

    hours = [h for h,_ in track_list]
    counts = [c for _, c in track_list]

    total_hours = sum(hours)
    average_hours = total_hours / len(hours)

    total_counts = sum(counts)
    average_counts = total_counts / len(counts)

    label_list = []
    for focus_hours,distraction_counts in track_list:
        if distraction_counts > focus_hours:
            label_list.append('Bad day')
        else:
            label_list.append('Good day')
    
    

    if total_counts > total_hours:
        result = 'Need discipline'
    else: 
        result = 'On the right path'

    print(f'\n{name} focus analyzer.')
    print(f'-------------------------')

    for i,(h,c,l) in enumerate(zip(hours,counts,label_list),start = 1):
        print(f'Day{i}: {h} focus hours. {c} distractions.- {l}')

    print(f'\nTotal focus hours: {total_hours}h')
    print(f'Average focus hours: {average_hours}h')
    print(f'Highest: {max(hours)}')
    print(f'Lowest: {min(hours)}')

    print(f'\nTotal distraction counts: {total_counts}')
    print(f'Average distraction counts: {average_counts:.2f}')
    print(f'Highest counts: {max(counts)}')
    print(f'Lowest counts: {min(counts)}')

    print(f'Result: {result}')

    repeat = input('Do you want repeat(yes/no): ').lower()
    if repeat != 'yes':
        break

input('Press enter to exit')



