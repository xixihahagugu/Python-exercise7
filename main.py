4.5

"""
Write a program that asks the user for a username and password.
If either or both are incorrect, the program ask the user to enter
the username and password again. This continues until the login
information is correct or wrong credentials have been entered five times.
If the information is correct, the program prints out Welcome.
After five failed attempts the program prints out Access denied.
The correct username is python and password rules.
"""

rounds = 0

while True:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    rounds = rounds + 1

    if username == "python" and password == "rules" :
        print("Welcome")
        break
    elif rounds > 5:
        print("Access denied")
        break

