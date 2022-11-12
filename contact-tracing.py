# This program allows you to save info of a person for the purpose of contact tracing
# Program created by: Jeferson A. Tadios

contact_list = {
    "Jeferson Tadios" : {
        "Age" : "20",
        "Address" : "306 Cluster 3 Flexihomes",
        "Contact#" : "01234567890"
        }
}

get_age = contact_list["Jeferson Tadios"]["Age"]
get_address = contact_list["Jeferson Tadios"]["Address"]
get_contact = contact_list["Jeferson Tadios"]["Contact#"]


print("Menu:"+
"\n1 -> Add an Item"+
"\n2 -> Search"+
"\n3 -> Exit")

user_input = int(input("What do you want to do? "))

if user_input == 1:
    print("Option 1")
elif user_input == 2:
    print("Option 2")
elif user_input == 3:
    print("Option 3")
else:
    print("Invalid Option")
