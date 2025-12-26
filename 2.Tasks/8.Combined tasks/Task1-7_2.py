

def get_site_info():
    
    while True:
        name = input("Tell me site name: ").strip()
        if name == "":
            print("Cannot be empty")
        else:
            name = name.capitalize()
            break

    while True:
        day = input("Tell me the work day: ").strip()
        if day == "":
            print("Cannot be empty")

        else:
            day = day.upper()
            break

    return name,day

def get_worker_count():
    while True:
        workers_count = input("Number of workers: ")
        if workers_count.isdigit() and int(workers_count) > 0:
            workers_count = int(workers_count)
            return workers_count

        else:
            print("Must be a positive number")
            

def get_worker_data():
    
    workers_count = get_worker_count()
    while True:
        worker_name = input("Worker name: ").strip()
        if worker_name == "":
            print("Cannot be empty")
        else:
            worker_name = worker_name.capitalize()
            break

    while True:
        hours = input()
