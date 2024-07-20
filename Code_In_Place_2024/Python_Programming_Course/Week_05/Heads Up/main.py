import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'
lines = []
def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    #lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines

def gen_random_word():
    for value in lines:
        index=random.randint(0,len(lines))
        guess_word=lines[index]
        print(guess_word)
        user_guess=input("Please share your guess word?")
        if user_guess==guess_word:
            print("Woah! Your guess is correct!")
        else:
            print("Woops! Better Luck Next time.")
    
    #for value in lines:
       # print(value)
def main():
    # your code here :) 
    words_list=get_words_from_file()
    print(words_list)
    gen_random_word()
    

if __name__ == '__main__':
    main()