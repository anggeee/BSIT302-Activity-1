print("Main Menu")

data = True

my_empty = []
while data:

    my_list = ("""
        0. Create a Student
        1. Read Student or Show Student
        2. Update Student Info
        3. Delete Student
        4. Exit
        """)
    print(my_list)
    num = (input("Enter a number "))

    if num == "0":
        name = (input("Enter name: "))
        my_empty.append(name)
        print("Done")
    elif num == "1":
        print(my_empty)
    elif num == "2":
        index = int(input("Index: "))
        newname = input("Enter New Name: ")
        my_empty[index] = newname
        print("Save Changes")
    elif num == "3":
        delname = input("Enter name to delete: ")
        my_empty.remove(delname)
        print("Deleted")
    elif num == "4":
        print("Goodbye!")
        data = False
    else:
        data = True
        print("Invalid number")
