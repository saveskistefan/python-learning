
def greet_user():
    name = input("Tell me your name: ").strip()

    if name == "":
        print("No name entered")
    else:
        print(f"Hello", name)
    
greet_user()

