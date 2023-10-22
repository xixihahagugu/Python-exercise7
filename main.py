# Exercise 4.2

"""
Write a program that converts inches to centimeters until the user inputs a
negative value. Then the program ends.
"""

while True:
    inches = float(input("Enter inches: "))

    if inches > 0:
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters:.2f} centimeters")
    else:
        print("Negative values, Program ends")
        break

