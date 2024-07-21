def get_number_from_user():
    #[2,5,7,8,3,4,2,7,0,2]
    number_list=[]
    while True:
        user_input=input("Enter any number:")
        #number_list=int(number_list)
        if user_input=="":
            break
        num=int(user_input)
        number_list.append(num)
     
    print(number_list)


get_number_from_user()