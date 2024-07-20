import random

def main():
    ##game=[0,1,2,3,4]
    game=['Julie','Mehran','Simba','Ayesha','Karel']
    max_index=len(game)-1
    #print(max_index)
    guess_index=random.randint(0,max_index)
    #print(guess_index)
    correct_string=game[guess_index]
    #print(correct_string)
    print("Guess the value from the following list\n")
    for i in game:
        print(i)
    user_input=input("Enter a guessing string from the above:\n ")
    
    if user_input==correct_string:
        print("Correct Answer")
    else:
        print("Wrong Answer.The correct answer is",correct_string)


if __name__=='__main__':
    main()


