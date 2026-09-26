from checker import check_strength
from validator import validate_password
from generator import generate_password
from history import save_history, view_history
from utils import title

while True:

    title("PASSWORD STRENGTH CHECKER")

    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. View History")
    print("4. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        password = input("\nEnter Password: ")

        valid, message = validate_password(password)

        if not valid:
            print("Error:", message)
            continue

        strength, score, feedback = check_strength(password)

        print("\nRESULT")
        print("-" * 30)
        print("Password :", "*" * len(password))
        print("Score    :", score, "/5")
        print("Strength :", strength)

        if feedback:
            print("\nSuggestions:")
            for i in feedback:
                print("•", i)
        else:
            print("\nExcellent Password!")

        save_history(password, strength)

    elif choice == "2":

        pwd = generate_password()
        print("\nGenerated Password:", pwd)

    elif choice == "3":

        view_history()

    elif choice == "4":

        print("\nThank you!")
        break

    else:
        print("\nInvalid Choice.")