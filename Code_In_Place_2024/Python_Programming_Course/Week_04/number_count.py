def get_number_from_user():
    #[2,5,7,8,3,4,2,7,0,2]
    number_list=[]
    while True:
        user_input=input("Enter any number:")
        #number_list=int(number_list)
        if user_input=="":
            break
        #type_casting_concept
        num=int(user_input)
        number_list.append(num)
     
    return number_list

def count_number(num_lst):
    #num_dict={'value_of_user_entry':'number_of_times_he entered_the_number'}
    num_dict = {}
    for num in num_lst:
        #unique_number_in_list
        if num not in num_dict:
            num_dict[num] = 1
        else:
        #repetitive_number_in_list
            num_dict[num] += 1
    
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

number_list=get_number_from_user()
print_count=count_number(number_list)
print(print_count)
