birthday = {
    'ashish' : '08-08-98'
}

def show_menu():
    print("\n*****WELCOME TO BIRRTHDAY CALENDER*****")
    print("Enter the operation you want to perform.")
    print("---------------------")
    print("\t1. View Birthday")
    print("\t2. Add Birthday")
    print("\t3. Update Birthday")
    print("\t4. Remove Birthday")
    print("\t5. View all Birthdays")
    print("\t6. Exit")
    print("----------------------")


def display():
    print("*****BIRTHDAYS LIST*****")
    print("-----------")
    for key, value in birthday.items():
        print("{} : {}".format(key,value))

while True:
    show_menu()

    choice = input()

    if choice == '1':
        name = input("Enter the person's name:")
        if name in birthday.keys():
            print("{} : {}".format(name, birthday[name]))
        else:
            print("no details found")

    elif choice == '2':
        name = input("Enter the name to add:")
        if name in birthday.keys():
            print("Already Exists")
        else:
            birth_date = input("Enter birthday for {}".format(name))
            birthday[name] = birth_date

    elif choice == '3':
        name = input("Enter name you want to update:")
        if name in birthday.keys():
            birth_date = input("Enter birthday for {}".format(name))
            birthday[name] = birth_date
        else:
            print("Doesn't exist")

    elif choice == '4':
        name = input("Enter name you want to remove:")
        if name in birthday.keys():
           del birthday[name]
           print("Successfully deleted")
        else:
            print("Doesn't exist")

    elif choice == '5':
       display()

    elif choice == '6':
        print("Have a good day.")
        break
    else:
        print("Sorry I cannot perform this operation")