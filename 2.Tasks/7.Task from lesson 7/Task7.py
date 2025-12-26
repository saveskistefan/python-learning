# My company data

while True:
    days = input("How many days you worked this week(1-7): ")
    if days.isdigit() and 1 <= int(days) <= 7:
        days = int(days)
        break

days_data = []
workers = 0
hours_work = 0

for i in range(days):
    material_per_day = []
    workers_on_site = int(input(f"Day{i+1}:How many workers were today: "))
    machines = int(input(f"Day{i+1}:How many machines worked today: "))
    materials = input(f"Day{i+1}:Material brought today: ")
    hours_worked = float(input(f"Day{i+1}:How many hours you worked today: "))

    workers += workers_on_site
    hours_work += hours_worked

    day = {
        'workers_on_site': workers_on_site,
        'machines': machines,
        'materials': materials,
        'hours_worked': hours_worked
    }

    days_data.append(day)


print(f"\nSummary")
print("-------------")

for i,day in enumerate(days_data,start=1):
    print(f"Day {i}"
          f"\n{day['workers_on_site']} workers. "
          f"{day['machines']} machines. "
          f"We brought: {day['materials']},  "
          f"{day['hours_worked']} hours.")
    
print(f"\nTotal workers: {workers}")
print(f"Total hours: {hours_work}")

input("Press enter to exit")
