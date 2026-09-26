import os

FILE = "data/history.txt"

def save_history(password, strength):
    os.makedirs("data", exist_ok=True)

    with open(FILE, "a") as f:
        f.write(f"{password} --> {strength}\n")

def view_history():
    if not os.path.exists(FILE):
        print("\nNo history available.")
        return

    print("\n------ PASSWORD HISTORY ------")

    with open(FILE, "r") as f:
        print(f.read())