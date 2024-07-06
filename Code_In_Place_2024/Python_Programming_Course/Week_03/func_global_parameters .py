
#Defining the variables

x=input("Enter first number:\n")
y=input("Enter second number:\n")
operator= input("Please choose any operation "+"+"+"-"+"-"+"\n")

#defining main function
def main():
    global x;global y;global operator
   #Performing operations as per the user requirement
    if operator=='+':
        sum=addition(x,y)
        print("The sum is:",sum)
    elif operator=='-':
        minus=subtraction(x,y)
        print("The difference  is:",minus)
    else:
        multiplication(x,y)
        print("The product is:",multiplication)

def addition(a,b):
    global x;global y
    return int(x)+int(y)

def subtraction(a,b):
    global x;global y
    return int(x)-int(y)

def multiplication(a,b):
    global x;global y
    return int(x)*int(y)

if __name__== '__main__':
    main()
    
    