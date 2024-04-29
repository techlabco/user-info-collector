import json

def get_input(prompt, validation_func):
    while True:
        data = input(prompt)
        if validation_func(data):
            return data
        else:
            print("Invalid input. Please try again.")

def get_hobbies():
    hobbies = []
    while True:
        hobby = input("Enter a hobby (type 'done' when finished): ")
        if hobby.lower() == 'done':
            break
        elif hobby:  # check if hobby is not an empty string
            hobbies.append(hobby)
        else:
            print("Invalid input. Please try again.")
    return hobbies

def save_user_info(name, age, hobbies):
    user_info = {
        "name": name,
        "age": age,
        "hobbies": hobbies
    }
    try:
        with open("user_info.json", "w") as file:
            json.dump(user_info, file)
    except IOError:
        print("Error writing to file. Please check if the file is open in another program.")

def main():
    name = get_input("Enter your name: ", lambda x: x)
    age = get_input("Enter your age: ", lambda x: x.isdigit() and int(x) > 0)
    print("Enter your hobbies (type 'done' when finished):")
    hobbies = get_hobbies()
    
    save_user_info(name, age, hobbies)
    
    print("\nName:", name)
    print("Age:", age)
    print("Hobbies:", ", ".join(hobbies))

if __name__ == "__main__":
    main()