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

print (get_age)
print (get_address)
print (get_contact)