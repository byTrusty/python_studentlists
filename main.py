data = {
    1: {"name": "Alice", "hometown": "New York", "favorite_food": "Pizza"},
    2: {"name": "Bob", "hometown": "Los Angeles", "favorite_food": "Tacos"},
    3: {"name": "Charlie", "hometown": "Chicago", "favorite_food": "Burgers"},
    4: {"name": "Andrew", "hometown": "Detroit", "favorite_food": "Ribs"}
}

while True:
    choice = input("Enter a number (1-4) or name to choose a student, or 'l' to see a list of student names, or 'q' to quit: ")
    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == 'l':
        print("List of students:")
        for student in data.values():
            print(student['name'])
        continue
    elif choice in [str(i) for i in range(1, 5)] or choice in [student['name'] for student in data.values()]:
        while True:
            if choice in [str(i) for i in range(1, 5)]:
                student = data[int(choice)]
            else:
                student = next((item for item in data.values() if item["name"] == choice), None)
            print(f"{student['name']} - Enter 'hometown' or 'favorite food' to learn more, 'n' to select another student, 'l' to see the list of student names, or 'q' to quit.")
            info = input()
            if info == 'q':
                break
            elif info == 'n':
                break
            elif info == 'hometown':
                print(f"{student['name']}'s hometown is {student['hometown']}.")
            elif info == 'favorite food':
                print(f"{student['name']}'s favorite food is {student['favorite_food']}.")
            elif info == 'l':
                print("List of students:")
                for student in data.values():
                    print(student['name'])
                continue
            else:
                print("Invalid input, please try again.")
            cont = input("Would you like to learn about another student? Enter 'y' for yes, or 'n' for no: ")
            if cont.lower() == 'n':
                break
            elif cont.lower() == 'y':
                choice = input("Enter a number (1-4) or name to choose another student: ")
                if choice == 'q':
                    print("Goodbye!")
                    break
                elif choice == 'l':
                    print("List of students:")
                    for student in data.values():
                        print(student['name'])
                    break
                elif choice in [str(i) for i in range(1, 5)] or choice in [student['name'] for student in data.values()]:
                    continue
                else:
                    print("Invalid input, please try again.")
                    continue
    else:
        print("Invalid input, please try again.")
