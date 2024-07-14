#checks whether the number is within the range specified
def range_number(number,start,stop):
    if number in range(start,stop):
        print(number,"is in range",start,"-->",stop)
    else:
        print(number,"is out of range",start,"-->",stop)
    return number,start,stop
     
def main():
    number = int(input("Enter the number to check\n"))
    start = int(input("Enter the start range\n"))
    stop = int(input("Enter the stop range\n"))
    range_num=range_number(number,start,stop)
    print(range_num)

if __name__=='__main__':
    main()