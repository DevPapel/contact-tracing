# This program allows you to save info of a person for the purpose of contact tracing
# Program created by: Jeferson A. Tadios

contact_list = {
    "Jeferson Tadios" : {
        "Age" : "20",
        "Address" : "306 Cluster 3 Flexihomes",
        "Contact#" : "01234567890"
        }
}

print("Menu:"+
"\n1 -> Add an Item"+
"\n2 -> Search"+
"\n3 -> Exit")

menu_input = int(input("What do you want to do? "))
user_input = input("Enter the Full name: ")

get_age = contact_list[user_input]["Age"]
get_address = contact_list[user_input]["Address"]
get_contact = contact_list[user_input]["Contact#"]


if menu_input == 1:
    print("Option 1")
elif menu_input == 2:
    print("Getting info of:",user_input)
    print("Age: "+str(get_age)+
    "\nAddress: "+str(get_address)+"\nContact#: "+
    str(get_contact))
elif menu_input == 3:
    print("Option 3")
else:
    print("Invalid Option")
