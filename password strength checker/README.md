# Password Strength Checker

## 1. Project Overview

Password Strength Checker is a Python-based project that evaluates the strength of a password using different security criteria. It checks password length, uppercase letters, lowercase letters, numbers, and special characters.

The project also provides a strong password generator and a history feature for previously checked passwords.

## 2. Problem Statement

Many users create weak passwords that are easy to guess. A password should contain a suitable combination of characters to improve security.

This project provides a simple way to check password strength and gives suggestions for improving weak passwords.

## 3. Objectives

* To check the strength of a password.
* To identify missing password requirements.
* To generate strong random passwords.
* To validate user input.
* To maintain a record of password-checking results.
* To demonstrate Python programming concepts in a practical project.

## 4. Features

### Password Strength Checker

Checks the password using five criteria:

1. Minimum length of 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

### Password Generator

Generates a random password using:

* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

### Input Validation

Checks whether:

* The password is empty.
* The password contains spaces.

### History

Stores password-checking results in a text file.

## 5. Strength Levels

| Score | Strength    |
| ----- | ----------- |
| 0-1   | Very Weak   |
| 2     | Weak        |
| 3     | Medium      |
| 4     | Strong      |
| 5     | Very Strong |

## 6. Technologies Used

* Python
* Python Standard Library
* VS Code
* Git
* GitHub

## 7. Python Concepts Used

* Variables
* Conditional statements
* Loops
* Functions
* Strings
* Lists
* File handling
* Modules
* Exception and input validation concepts
* Random password generation

## 8. Project Structure

```text
Password_Strength_Checker/
│
├── main.py
├── checker.py
├── validator.py
├── generator.py
├── history.py
├── utils.py
├── test_checker.py
├── README.md
├── statement.md
│
└── data/
    └── history.txt
```

## 9. How to Run

### Step 1

Install Python on your computer.

### Step 2

Open the project folder in VS Code.

### Step 3

Open `main.py`.

### Step 4

Run:

```bash
python main.py
```

## 10. Menu Options

The program provides four options:

```text
1. Check Password Strength
2. Generate Strong Password
3. View History
4. Exit
```

## 11. Testing

The project includes `test_checker.py` for testing the password-strength checking function.

Run the tests using:

```bash
python test_checker.py
```

## 12. Sample Output

```text
=============================================
         PASSWORD STRENGTH CHECKER
=============================================

1. Check Password Strength
2. Generate Strong Password
3. View History
4. Exit

Enter choice: 1

Enter Password: Hello123@

RESULT
------------------------------
Password : *********
Score    : 5 /5
Strength : Very Strong

Excellent Password!
```

## 13. Future Enhancements

* Graphical user interface using Tkinter
* Password entropy calculation
* Common-password detection
* Better password history privacy
* More advanced password security analysis
* Exporting results into a report file

## 14. Conclusion

The Password Strength Checker demonstrates how Python programming concepts can be combined to solve a practical problem. The project uses modular programming, input validation, file handling, password generation, and automated testing.
