

def get_site_info():
    while True:
        name = input("Tell me the site name: ").strip()
        if name == "":
            print("Cannot be empty")
        else:
            name = name.capitalize()
            break

    while True:
        work_day = input("Tell me the work day: ").strip()
        if work_day == "":
            print("Cannot be empty")
        else:
            work_day = work_day.upper()
            break

    return name,work_day

def get_worker_count():
    while True:
        workers_count = input("How many workers came: ")
        if workers_count.isdigit() and int(workers_count) > 0:
            workers_count = int(workers_count)
            return workers_count
        else:
            print("Must be a postive number")


work_info = get_site_info()
workers_count = get_worker_count()


workers_list = []

def get_worker_data():

    for i in range(workers_count):
        skip_worker = False
        while True:
            name = input(f"Worker {i+1}: Name ->: ")
            if name == "":
                print("Must not be empty")
            else:
                name = name.capitalize()
                break
        
        while True:
            hours = input(f"Worker {i+1}: Hours worked ->: ")
            
            if hours == "0":
                print("Skipping worker")
                break
        
            
            hours = hours.replace(',','.')

            if hours.replace('.','',1).isdigit():
                hours = float(hours)
                if 1 <= hours <= 16:
                    break
            else:
                print("Invalid number")

        while True:
            quality = input(f"Worker {i+1}: Quality ->: ")

            if quality.isdigit() and 1 <= int(quality) <= 10:
                quality = int(quality)
                break
            else:
                print("Invalid number")
       
        if skip_worker == "0":
            continue

        if hours < 6:
            status = "Underworked"

        elif quality <= 4:
            status = "Low quality"
        

        worker = {
            "name": name,
            "hours": hours,
            "quality":quality,
            "status": status
            }

        workers_list.append(worker)

    return workers_list 

workers_list = get_worker_data()

worker = [worker for worker in workers_list]

hours = [w["hours"]for w in workers_list]
quality = [w["quality"] for w in workers_list]

total_hours = sum(hours)
average_hours = total_hours / len(hours)

total_quality = sum(quality)
average_quality = total_quality / len(quality)

best_worker = max(workers_list, key=lambda w: w["quality"])
worst_worker = min(workers_list, key=lambda w: w["quality"])

name_site,work_day =  work_info


if average_quality >= 8 and average_hours >=8:
    rating = "Excellent"
elif average_quality >= 6 and average_hours >=7:
    rating = "Good"
elif average_quality >= 5:
    rating = "Average"
else:
    rating = "Poor"

print(f"\nSITE: {name_site}")
print(f"Day: {work_day}")

print(f"\nWorkers: {workers_count}")
print(f"Total hours: {total_hours}")
print(f"Average hours: {average_hours:.1f}")
print(f"Average quality: {average_quality:.1f}")

print(f"Best worker: {best_worker['name']} ({best_worker['quality']})")
print(f"Worst worker: {worst_worker['name']} ({worst_worker['quality']})")

print(f"Day rating: {rating}")

input("Press enter to exit")
    





        

            

            


    