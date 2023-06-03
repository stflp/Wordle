import functions as func


while True:
    print("1. Login\n2. Register\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        func.login()
    elif choice == '2':
        while True:
            print()
            username = input("Username: ")
            if username in [user[0] for user in func.users]:
                print("Username already exists.\n")
            else:
                password = input("Password: ")
                func.users.append([username, password])
                with open("usersdb.txt", "a") as db:
                    db.write(username + "," + password + ",0,0,0,0,0,0,0,0\n")
                print("Username registered successfully.\n")
                break
    elif choice == '3':
        exit()
    else:
        print("\nPlease enter 1, 2 or 3.")