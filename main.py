# 7.2

names = set()

while True:
    names_input = input("Enter your name (or an empty string to quit): ")

    if names_input == "":
        break

    if names_input in names:
        print("Existing name")
    else:
        print("New name")
        names.add(names_input)

print(names)



