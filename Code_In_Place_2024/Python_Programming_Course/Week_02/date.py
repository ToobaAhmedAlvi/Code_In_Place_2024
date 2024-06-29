#Importing a library
import datetime
global date_now

def main():
    pass
    #date()


def date():
    date_now=datetime.datetime.today()
    print(date_now)

if __name__== '__main__':
    main()
    date()





'''
#time 

import time

timestamp = time.time()
current_date = time.ctime(timestamp)
print(current_date)

'''