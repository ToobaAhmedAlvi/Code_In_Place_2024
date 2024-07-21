my_dict={}
while True:
    name=input("Enter your name:")
    number=input("Enter your contact")
    #dict_name[key]=value
    my_dict[name]=number
    print(my_dict)
    if name=='':
        break
    print(my_dict.keys)
    print(my_dict.values)

