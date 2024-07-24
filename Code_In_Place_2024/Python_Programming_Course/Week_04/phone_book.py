def make_phone_book():
    my_dict={}
    while True:
        name=input("Enter your name:")   
        if name=="":
            break
        number=input("Enter your contact")
        my_dict[name]=number    
        print(my_dict.keys)
        print(my_dict.values)
    return my_dict

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(str(name) + " -> " + str(phonebook[name]))

def main():
    phonebook = make_phone_book()
    print(phonebook)
    lookup_numbers(phonebook)
   


# Python boilerplate.
if __name__ == '__main__':
    main()
