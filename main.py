choose=input("Choose an option:Enter a new airport,Fetch the information of an existing airport or Quit:")
airport_dictionary={}
airport_dictionary["EBAW"]="Antwerp InternationalAirport"
airport_dictionary["EKBI"]="Billund Airport"
airport_dictionary["EFHK"]="Helsinki-Vantaa Airport"
airport_dictionary["EPBC"]="Warszawa-Babice Airport"

while choose=="Enter a new airport":

    new_ICA0_code=input("Enter the ICA0 code:")

    new_airport_name=input("Enter airport name:")

    airport_dictionary[new_ICA0_code]=new_airport_name

    print(airport_dictionary)
    break

choose =input("Choose an option:Enter a new airport,Fetch the information of an existing airport or Quit:")
while choose=="Fetch the information":
    ICA0_code=input("enter the ICA0 code:")
    if ICA0_code in airport_dictionary:
        print(f"{ICA0_code}is the {airport_dictionary[ICA0_code]}")
choose =input("Choose an option:Enter a newairport,Fetch the information of an existingairport or Quit:")
while choose=="Quit":
    break
choose =input("Choose an option:Enter a new airport,Fetch the information of an existing airport or Quit:")






