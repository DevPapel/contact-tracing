# This program allows you to save info of a person for the purpose of contact tracing
# Program created by: Jeferson A. Tadios

def main():
    if menu_input == 1:
        user_input1 = input("Enter the Full name: ")
        while user_input1 in contact_list:
            print(user_input1,"is already in the contact list")
            user_input1 = input("Enter the Full name: ")
        user_input2 = input("Enter the Age: ")
        user_input3 = input("Enter the Address: ")
        user_input4 = input("Enter the Contact#: ")
        contact_list[user_input1] = {
            "Age":user_input2,
            "Address":user_input3,
            "Contact#":user_input4
        }
        print(contact_list)
    elif menu_input == 2:
        user_input = input("Enter the Full name: ")
        get_age = contact_list[user_input]["Age"]
        get_address = contact_list[user_input]["Address"]
        get_contact = contact_list[user_input]["Contact#"]
        print("Getting info of:",user_input)
        print("Age: "+str(get_age)+
        "\nAddress: "+str(get_address)+"\nContact#: "+
        str(get_contact))
    elif menu_input == 3:
        print("Thank you for using this program! Have a nice day")
        exit()
    else:
        print("Invalid Option")
    cont()

def cont():
    print("")
    continue_prog = input("Do you want to continue? [Y/N]: ").upper()
    if continue_prog != "Y":
        exit()

def showMenu():
    print("Menu:"+
"\n1 -> Add an Item"+
"\n2 -> Search"+
"\n3 -> Exit")




contact_list = {
    "Jeferson Tadios" : {
        "Age" : "20",
        "Address" : "306 Cluster 3 Flexihomes",
        "Contact#" : "01234567890"
        }
}



while True:
    showMenu()
    menu_input = int(input("What do you want to do? "))
    main()


