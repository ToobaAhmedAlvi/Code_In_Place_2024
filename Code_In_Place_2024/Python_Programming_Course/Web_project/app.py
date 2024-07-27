from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(name): 
    name=input("Enter name:")
    print(name)
  
if __name__=='__main__': 
   app.run() 