import random
from colorama import Fore

with open('words.txt', 'r') as words_db:
    words = [line.strip().upper() for line in words_db]

with open("usersdb.txt", "r") as users_db:
    users = [line.strip().split(",") for line in users_db]

def gameplay(user):
    while True:
        correct_word = random.choice(words)
        if(len(user) == 2):
            user.extend(['0', '0', '0', '0', '0', '0', '0', '0'])
        user[2] = str(int(user[2]) + 1)
        for i in range(6):
            while True:
                guess = input("Your guess: ")
                guess = guess.upper()
                if len(guess) == 5 and guess in words:
                    break
                print("Invalid word.")

            if guess == correct_word:
                print('\n' + Fore.GREEN + guess + Fore.RESET + ' is the correct word!')
                print("Guessed in " + str(i + 1) + " tries.")
                user[3] = str(int(user[3]) + 1)
                user[i+4] = str(int(user[i+4]) + 1)
                show_stats(user)
                update_user_credentials(user)
                loop = input("Try again?\nType 'continue' to continue. Type anything else to exit. ")
                loop = loop.lower()
                if(loop != 'continue'):
                    return exit()
                print()
            else:
                guessed = ''
                for j in range(5):
                    if guess[j] == correct_word[j]:
                        guessed += Fore.GREEN + guess[j] + Fore.RESET
                    elif guess[j] in correct_word:
                        guessed += Fore.YELLOW + guess[j] + Fore.RESET
                        
                    else:
                        guessed += guess[j]
                print("Feedback: " + guessed + "\n")
        else:
            print('You ran out of guesses. The correct word was ' + Fore.RED + correct_word + Fore.RESET + '.')
            show_stats(user)
            update_user_credentials(user)
            loop = input("Try again?\nType 'continue' to continue. Type anything else to exit. \n")
            loop = loop.lower()
            if(loop != 'continue'):
                exit()
            print()

def login():
    while True:
        username = input("\nUsername: ")
        if username not in [user[0] for user in users]:
            print("\nUsername does not exist.\n")
            break
        else:
            password = input("Password: ")
            if [username, password] in [user[:2] for user in users]:
                print()
                user = get_user_credentials_from_username(username)
                gameplay(user)
        print("\nInvalid credentials.\n")

def get_user_credentials_from_username(username):
    for user in users:
        if user[0] == username:
            return user
    return None

def update_user_credentials(user):
    for i in range(len(users)):
        if users[i] == user:
            users[i] = user
            break
    with open("usersdb.txt", "w") as users_db:
        for user in users:
            users_db.write(user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + user[4] + "," + user[5] + "," + user[6] + "," + user[7] + "," + user[8] + "," + user[9] + "\n")


def show_stats(user):
    if(user[2]>'0'):
        winrate = round(int(user[3]) / int(user[2]) * 100, 2)
    else:
        winrate = 0
    print(user[2] + ' matches played.\n' + user[3] + ' matches won.\n' + str(winrate) + '% win rate.')
    print("Guessed in 1 try: " + str(int(user[4])) + "\nGuessed in 2 tries: " + str(int(user[5])) + "\nGuessed in 3 tries: " + str(int(user[6])) + "\nGuessed in 4 tries: " + str(int(user[7])) + "\nGuessed in 5 tries: " + str(int(user[8])) + "\nGuessed in 6 tries: " + str(int(user[9])) + "\n")