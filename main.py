gender =input("Enter your biological gender:")
while gender =="Female":
    value =int(input("Enter your hemoglobin value(g/l):"))

    if value<117:
        print("The hemoglobin value is low")
        break

    elif value>155:
        print("The hemoglobin value is high")
        break

    else:
        print("The hemoglobin value is normal")
        break
while gender =="Male":
    value =int(input("Enter your hemoglobin value(g/l):"))

    if value<134:
        print("The hemoglobin value is low")
        break

    elif value>167:
        print("The hemoglobin value is high")
        break

    else:
        print("The hemoglobin value is normal")
        break