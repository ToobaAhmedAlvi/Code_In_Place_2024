from graphics import Canvas
#from graphics import Canvas
import os
import random
import math
import time
from graphics import * 
global answer    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
DELAY=2
def welcome_message():
    global oval
    oval = canvas.create_oval(
    10, 
    10, 
    390, 
    290,
    "yellow",
    "LightGreen"
)
    welcome_message=canvas.create_text(
    40, 
    100, 
    text = """Welcome to Flag Guessing Game!"""   ,
    font = 'Garamond', 
    font_size = 25, 
    color ='Red')
    time.sleep("3")
    
    
    instruction=canvas.create_text(
    35, 
    150, 
    text = """Click on screen to continue reading instructions to play.>>"""   ,
    font = 'Garamond', 
    font_size = 15, 
    color ='Magenta')
    canvas.wait_for_click()
    canvas.change_text(instruction,"This game requires minimal knowledge about Country flags.")
    canvas.wait_for_click()
    canvas.delete(welcome_message)
    canvas.delete(instruction)
    canvas.delete(oval)
    instruction_1=canvas.create_text(
    10, 
    50, 
    text = """ "GAME INSTRUCTIONS"  """   ,
    font = 'Garamond', 
    font_size = 20, 
    color ='MAROON')
    
    instruction_2=canvas.create_text(
    10, 
    100, 
    text = """-> 5 Flags will be shown on screen."""   ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Green')
    canvas.wait_for_click()
    instruction_3=canvas.create_text(
    10, 
    120, 
    text = """-> You'll be given 10 secs to guess each of them."""   ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Blue')
    canvas.wait_for_click()
    instruction_4=canvas.create_text(
    10, 
    140, 
    text = """-> By showing the 1st flag, You'd be asked to guess the country name on console."""   ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Brown')
    canvas.wait_for_click()
    instruction_5=canvas.create_text(
    10, 
    160, 
    text = """-> If you don't know the answer, please write Pass/NA. """   ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Red')
    canvas.wait_for_click()
    instruction_6=canvas.create_text(
    10, 
    180, 
    text = """-> The flag will change after 10 secs, & You'll be asked for another guess.""" ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Lightblue')
    canvas.wait_for_click()
    instruction_7=canvas.create_text(
    10, 
    200, 
    text = """-> This process continues untill all 5 flag are displayed on the screen. """ ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Purple')
    canvas.wait_for_click()
    instruction_8=canvas.create_text(
    10, 
    220, 
    text = """-> To every correctly guessed flag, 10 points will be added to your score. """ ,
    font = 'Garamond', 
    font_size = 12, 
    color ='Black')
    canvas.wait_for_click()
    instruction_9=canvas.create_text(
    10, 
    240, 
    text = """-> You better make a guess (No negative marking for making a wrong guess).""" ,
    font = 'Garamond', 
    font_size = 12, 
    color ='LightGreen')
    canvas.wait_for_click()
    instruction_10=canvas.create_text(
    200, 
    260, 
    text = """CLICK TO START>>""" ,
    font = 'Garamond', 
    font_size = 20, 
    color ='Orange'
    )
    canvas.wait_for_click()
    canvas.delete(instruction_1) 
    canvas.delete(instruction_2)
    canvas.delete(instruction_3)
    canvas.delete(instruction_4)
    canvas.delete(instruction_5)
    canvas.delete(instruction_6)
    canvas.delete(instruction_7)
    canvas.delete(instruction_8)
    canvas.delete(instruction_9)
    canvas.delete(instruction_10)  
    game_ready()

def game_ready():
    rect = canvas.create_rectangle(
    0, 
    0, 
    CANVAS_WIDTH, 
    CANVAS_HEIGHT,
    "black",
    "white"
)
    game_ready=canvas.create_text(
    30, 
    100, 
    text = """BE PATIENT. THE GAME WILL START IN 5 SECONDS. ALL THE BEST!""" ,
    font = 'Garamond', 
    font_size = 15, 
    color ='Orange'
    )
    return game_ready
   

def flag_Japan():
    country_serial=1
    #canvas.create_oval(CANVAS_WIDTH/2,200,CANVAS_WIDTH/2+70,175, color="#A020F0")
    canvas.create_rectangle(0,0,400,300,"white")
    canvas.create_oval(100,50,300,250, color="red")
    

def flag_Russia():
    country_serial=2
    #define coordinates for 1st rectangle
    left_x=0
    top_y=0
    right_x=left_x+CANVAS_WIDTH
    bottom_y=top_y+100
    #TODO, create 1st rectangle
    canvas.create_rectangle(left_x,top_y,right_x,bottom_y,"white")
    #define coordinates for 2nd rectangle
    left_x2=0
    top_y2=100
    right_x2=left_x2+CANVAS_WIDTH
    bottom_y2=top_y2+100
    # TODO, create 1st rectangle
    canvas.create_rectangle(left_x2,top_y2,right_x2,bottom_y2,"blue")
    #define coordinates for 3rd rectangle
    left_x3=0
    top_y3=200
    right_x3=left_x3+CANVAS_WIDTH
    bottom_y3=top_y3+100
    canvas.create_rectangle(left_x3,top_y3,right_x3,bottom_y3,"red")

  
def flag_Pakistan():
    country_serial=3

    canvas.create_rectangle(0,0,400,400,"green")
    canvas.create_rectangle(0,0,125,400,"white")
    canvas.create_oval(200,75,375,225, color="white")
    canvas.create_oval(220,50,400,220, color="green")
    canvas.create_line(275, 125, 260, 175,color="white")
    canvas.create_line(275, 125, 290, 175,"white")
    canvas.create_line(275, 125, 260, 175,"white")
    canvas.create_line(275, 125, 290, 175,"white")
    canvas.create_line(250, 145, 300, 145,"white")
    canvas.create_line(250, 145, 300, 145,"white")
    canvas.create_line(250, 145, 290, 175,"white")
    canvas.create_line(250, 145, 290, 175,"white")
    canvas.create_line(260, 176, 300, 145,"white")
    canvas.create_line(260, 176, 300, 145,"white")
  
def flag_USA():
    country_serial=4
    canvas.create_rectangle(0,0,400,23,"darkred")
    canvas.create_rectangle(0,23,400,46,"white")

    canvas.create_rectangle(0,46,400,69,"darkred")
    canvas.create_rectangle(0,69,400,92,"white")

    canvas.create_rectangle(0,92,400,115,"darkred")
    canvas.create_rectangle(0,115,400,138,"white")

    canvas.create_rectangle(0,138,400,161,"darkred")
    canvas.create_rectangle(0,161,400,184,"white")

    canvas.create_rectangle(0,184,400,207,"darkred")
    canvas.create_rectangle(0,207,400,230,"white")

    canvas.create_rectangle(0,230,400,253,"darkred")
    canvas.create_rectangle(0,253,400,276,"white")

    canvas.create_rectangle(0,276,400,300,"darkred")
    #creating upside and down polygon
    canvas.create_rectangle(0,0,150,161,"white")
    #creating upside and down polygon
    
    canvas.create_polygon(20,0,130,0,75,60, color="darkblue")
    canvas.create_polygon(20,161,130,161,75,100, color="darkblue",)
    #creating leftside and rightside polygon
    
    canvas.create_polygon(0,20,0,150,60,80, color="darkblue")
    canvas.create_polygon(150,20,150,140,90,80, color="darkblue",)
      
    canvas.create_rectangle(63,0,87,161,"white")
    canvas.create_rectangle(0,68,150,92,"white")

    canvas.create_rectangle(65,0,85,161,"darkred")
    canvas.create_rectangle(0,70,150,90,"darkred")

def flag_France():
    country_serial=8
    canvas.create_rectangle(0,0,133,300,"blue")
    canvas.create_rectangle(133,0,266,300,"white")
    canvas.create_rectangle(266,0,399,300,"red")
    
def flag_Germany():
    country_serial=7
    #define coordinates for 1st rectangle
    left_x=0
    top_y=0
    right_x=left_x+CANVAS_WIDTH
    bottom_y=top_y+100
    #TODO, create 1st rectangle
    canvas.create_rectangle(left_x,top_y,right_x,bottom_y,"black")
    #define coordinates for 2nd rectangle
    left_x2=0
    top_y2=100
    right_x2=left_x2+CANVAS_WIDTH
    bottom_y2=top_y2+100
    # TODO, create 2nd rectangle
    canvas.create_rectangle(left_x2,top_y2,right_x2,bottom_y2,"red")
    #define coordinates for 3rd rectangle
    left_x3=0
    top_y3=200
    right_x3=left_x3+CANVAS_WIDTH
    bottom_y3=top_y3+100
    canvas.create_rectangle(left_x3,top_y3,right_x3,bottom_y3,"yellow")

def flag_United_Arab_Emirates():
    country_serial=5
    canvas.create_rectangle(0,0,120,300,"darkred")
     #define coordinates for 1st rectangle
    left_x=120
    top_y=0
    right_x=left_x+CANVAS_WIDTH
    bottom_y=top_y+100
    #TODO, create 1st rectangle
    canvas.create_rectangle(left_x,top_y,right_x,bottom_y,"green")
    #define coordinates for 2nd rectangle
    left_x2=120
    top_y2=100
    right_x2=left_x2+CANVAS_WIDTH
    bottom_y2=top_y2+100
    # TODO, create 2nd rectangle
    canvas.create_rectangle(left_x2,top_y2,right_x2,bottom_y2,"white")
    #define coordinates for 3rd rectangle
    left_x3=120
    top_y3=200
    right_x3=left_x3+CANVAS_WIDTH
    bottom_y3=top_y3+100
    canvas.create_rectangle(left_x3,top_y3,right_x3,bottom_y3,"black")

def flag_England():
    country_serial=9
    canvas.create_rectangle(0,0,400,300,"white")
    canvas.create_rectangle(170,0,230,300,"red")
    #define coordinates for 2nd rectangle
    left_x2=0
    top_y2=120
    right_x2=left_x2+CANVAS_WIDTH
    bottom_y2=top_y2+50
    canvas.create_rectangle(left_x2,top_y2,right_x2,bottom_y2,"red")

def flag_Italy():
    country_serial=6
    canvas.create_rectangle(0,0,133,300,"green")
    canvas.create_rectangle(133,0,266,300,"white")
    canvas.create_rectangle(266,0,399,300,"red")

def flag_Bangladesh():
    
    country_serial=10
    canvas.create_rectangle(0,0,400,400,"green")
    canvas.create_oval(100,50,300,250, color="red")
          
def user_input():
    global answer
    
    t1 = time.time()
    #print(t1)
    answer = input("Enter Country name you see on your screen:\n")
    t2 = time.time()
    #print(t2)
    t = t2 - t1
    print("Time taken to answer:",round(t),"seconds")
    if (t > 10) or (len(answer)==0):
        print("You have run out of time for this question!",round(t),"seconds")
        answer=""
        score=0
        
   
    return answer
     

def main():
    global score
    score=0
    list_answers=[]
    size=5
    len_answers=size
    
   
    # TODO: your code here!
   
    country_names={
        1:"JAPAN",
        2:"RUSSIA",
        3:"PAKISTAN",
        4:{"USA","US","AMERICA","UNITED STATES OF AMERICA","UNITED STATES"},
        5:{"UAE","UNITED ARAB EMIRATES"},
        6:"ITALY",
        7:"GERMANY",
        8:"FRANCE",
        9:"ENGLAND",
        10:"BANGLADESH"
           }  
    
    flag_serial=random.sample(range(1,10),5)
    
    for key,values in country_names.items():
        value=country_names[key]
        for i in flag_serial:
            if key==i:
                #print(i,value)
                                
                
                if key==1:
                    flag_Japan()                    
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)

                    
                    print("Current Score: ",score)
                  


                    
                elif key==2:
                    flag_Russia()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)

                elif key==3:
                    flag_Pakistan()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)

                
                elif key==10:
                    flag_Bangladesh()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                   
                    print("Current Score: ",score)
                    
                
                elif key==5:
                    flag_United_Arab_Emirates()
                    #user_input()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper() in value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)

                
                elif key==6:
                    flag_Italy()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)
                
                elif key==7:
                    flag_Germany()
                    user_input()
                    time.sleep(DELAY)
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)
                
                elif key==8:
                    flag_France()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper()==value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    print("Current Score: ",score)
                
                elif key==9:
                    flag_England()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper() == value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    
                    print("Current Score: ",score)

                                         
                elif key==4:
                    flag_USA()
                    time.sleep(DELAY)
                    user_input()
                    list_answers.append(answer)
                    if answer.upper() in value:
                        score+=10
                        print("Woah! You guessed it right.")
                    else:
                        score-=0
                        print("Wrongly guessed.The Correct answer is:",value)
                    print("Current Score: ",score)
    
    print("end")
    cls()
    print("Here's the list of your answers:\n")
    print(list_answers)
        
    if score>40 or score==40:
        print("Well Played! Your final Score: ", score)
    elif  score==30:
        print("Nice Try! Your final Score: ", score)
    else:
        print("Better Luck Next Time! Your final Score: ", score)


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def final_message():
   
    rectangle = canvas.create_rectangle(
    0,0,400,300, 
    "Pink", 
    "red")
    rectangle_up = canvas.create_rectangle(
    0,0,400,30, 
    "black", 
    "red")
    rectangle_down = canvas.create_rectangle(
    0,270,400,300, 
    "black", 
    "red")
    
    
    final_message=canvas.create_text(
    30, 
    120, 
    text = "Thank YOU for Playing!\nYour score: "+str(score),
    font = 'Garamond', 
    font_size = 22, 
    color ='Red')
    
    time.sleep("3")
    
        

if __name__ == '__main__':
    welcome_message()
    main()
    cls()
    final_message()
    
   