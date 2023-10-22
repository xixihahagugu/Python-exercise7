year =input("enter a year:")
x =int(year)
if x%100 ==0:
    if x%400 ==0:
        print("The year is leap")

    else:
        print("The year is not leap")
if x%100 !=0:
    if x%4 ==0:
            print("The year is leap")
    else:
        print("The year is not leap")

