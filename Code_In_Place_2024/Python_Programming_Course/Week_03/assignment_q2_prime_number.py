#prime number is only divisible by itself and 1
#whole numbers 0-infinity
#15 --> 1,3,5,15
def prime_number(number):
    if number<=1:
        print(number,"Not a prime number
        ")
    elif number>1:
        for i in range(2,number):
            if number%i==0:
                print(number,"Not a prime number")    
                break     
    
    elif number%i!=0:
        print(number,"a prime number")
    else:
        print("a prime number")         
          
    return number
    
def main():
    number=int(input("Enter a number to check:"))
    prime_number(number)
    
if __name__ =='__main__':
    main()
