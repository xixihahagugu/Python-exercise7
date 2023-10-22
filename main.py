"""
Write a program that asks the user to enter numbers until they
enter an empty string to quit. Finally, the program prints out
the smallest and largest number from the numbers it received.
"""


smallest = None
largest = None

while True:

    user = input("Enter a number (or press Enter to quit): ")

    if user == "":
        break

    try:
        number = float(user)

        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"The smallest number you received is {smallest} and the largest one is {largest}")

