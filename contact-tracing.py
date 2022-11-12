# This program allows you to save info of a person for the purpose of contact tracing
# Program created by: Jeferson A. Tadios

def main():
    if menu_input == 1:
        get_length = len(contact_list)
        print("\nShowing all the person that is saved on this contact tracing program"+
            "\nTotal Results:", get_length,"\n")
        for i in contact_list:
            print(" ●",i)

    elif menu_input == 2:
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
    elif menu_input == 3:
        user_input = input("Enter the Full name: ")
        while contact_list.get(user_input) is None:
            print("\nGetting info of:",user_input)
            print("There is no information about this person, Please try again\n")
            user_input = input("Enter the Full name: ")
        get_age = contact_list[user_input]["Age"]
        get_address = contact_list[user_input]["Address"]
        get_contact = contact_list[user_input]["Contact#"]
        print("\nGetting info of:",user_input)
        print("Age: "+str(get_age)+
        "\nAddress: "+str(get_address)+"\nContact#: "+
        str(get_contact))
    elif menu_input == 4:
        user_input1 = input("Enter the Full name of the information you want to change: ")
        while contact_list.get(user_input1) is None:
            print("\nThere is no information about",user_input1,"Please try again\n")
            user_input1 = input("Enter the Full name of the information you want to change: ")
        print("\nEdit Option"+
        "\n(1) Age"+"\n(2) Address"+"\n(3) Contact#")
        user_input2 = int(input("\nWhat do you want to edit? "))

    elif menu_input == 5:
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
    print("\n▁▂▃▄▅▆▇█ Main Menu █▇▆▅▄▃▂▁")
    print("\n   [1] ➪  Show Saved Contacts"+
        "\n   [2] ➪  Add an Item"+
        "\n   [3] ➪  Search"+
        "\n   [4] ➪  Edit Information"+
        "\n   [5] ➪  Exit\n")
    print("▁▂▃▄▅▆▇█████████████▇▆▅▄▃▂▁")




contact_list = {
    "Jeferson Tadios" : {
        "Age" : "20",
        "Address" : "306 Cluster 3 Flexihomes",
        "Contact#" : "01234567890"
        }
}


while True:
    showMenu()
    menu_input = int(input("\nWhat do you want to do? "))
    main()