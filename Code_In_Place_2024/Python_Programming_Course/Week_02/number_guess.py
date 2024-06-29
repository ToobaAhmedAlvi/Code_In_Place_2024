import random
def main():
    # Program selects a new random number
    secret_number = random.randint(1,100)
    print("I am thinking of a number from 1 to 100. What number am I thinking of?")
    guess_str = input()
    guess = int(guess_str)
    while guess != secret_number:
        if guess > secret_number:
            print("Nope! That guess was too high!")
        if guess < secret_number:
            print("Sorry! That guess was too low!")
        print("Take another guess!")
    guess_str = input()
    guess = int(guess_str)
    print("You guessed my number! Way to go!")
if __name__ == '__main__':
    main()
