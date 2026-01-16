

def get_gym_info():
    while True:
        name = input("Tell me your name: ").strip()
        if name == "":
            print("It cannot be empty")
        else:
            name = name.capitalize()
            break

    while True:
        day = input("What day is it?: ").strip()
        if day == "":
            print("It cannot be empty")
        else:
            day = day.upper()
            break

    return name,day

def get_trainee_count():
    while True:
        num_trainee = input("How many people trained today?: ")
        if num_trainee.isdigit() and int(num_trainee) > 0:
            num_trainee = int(num_trainee)
            break

    return num_trainee

num_trainee = get_trainee_count()
count_list = []

def get_trainee_data():
    for i in range(num_trainee):
        name_trainee = input(f"Trainee{i+1}: Name: ").strip()
        if name_trainee == "":
            print("Cannot be empty")
        else:
            name_trainee = name_trainee.capitalize()
            break

        minutes_trained = input(f"Trainee{i+1}: Minutes trained: ")
        minutes_trained.replace(",",".")

        if minutes_trained.replace(".","",1).isdigit() and 30 <= float(minutes_trained) <= 180:
            minutes_trained = float(minutes_trained)
            break
        else:
            print("Must be a postive number between 30 and 180")


        intensity_level = input(f"Trainee {i+1}: Tell me intensity level(1-10): ")
        if intensity_level.isdigit() and 1 <= int(intensity_level) <= 10:
            intensity_level = int(intensity_level)
            break
        
    return {
        "name_trainee": name_trainee,
        "minutes_trained": minutes_trained,
        "intensity_level": intensity_level
    }
trainees = []
count = get_trainee_data()

for _ in range(count):
    trainee = get_trainee_data()
    trainees.append(trainee)

print(trainees)

   






