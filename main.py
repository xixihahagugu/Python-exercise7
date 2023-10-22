# 7.2

names = set()

names_input = input("Enter your name(or an empty string to quit):")

while names_input != "":

    if names_input in names:

        print("Existing name")

    if names_input not in names:

        print("New name")

names.add(names_input)
names_input = input("Enter your name(or an empty string to quit):")
while names_input == "":
    break

print(names)



