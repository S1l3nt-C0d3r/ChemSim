

global ID
import pyrebase
config={
  "apiKey": "AIzaSyD_U2sGJigAYECFQmOQNdfu5s-Ybh3B5W0",
  "authDomain": "chemsimdb.firebaseapp.com",
  "projectId": "chemsimdb",
  "databaseURL":"https://chemsimdb-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "chemsimdb.appspot.com",
  "messagingSenderId": "862153368955",
  "appId": "1:862153368955:web:0cd213e8dce22ec75d49de",
  "measurementId": "G-PEBEQEN5FC"
        }
firebase=pyrebase.initialize_app(config)
database=firebase.database()
def setgame(name):
    global game
    game='g'+str(name)
    print(game)
def  checkscore(newscore):
    global ID
    global game
    a = dict(database.child("Users").child(ID).get().val())
    if newscore>a[game]:
        database.child("Users").child(ID).update({game: newscore})
    
    
def Login():
    global ID
    ID= input("User Id:")
    P=input("Password")
    try:
        a = dict(database.child("Users").child(ID).get().val())
        print(P)
        print(a["Password"])
        if P==a["Password"]:
            print("Welcome",a["Fname"])
            Action()
    except:
        print("USER ID Does not Exist")


def SignUp():
    ID=input("User Id:")
    P=input("Password")
    FN=input("FName")
    LN=input("LN")

    try:
        a = dict(database.child("Users").child("ID").get().val())
        print(a)
        print("USER ID Exists Try Again")
        SignUp()
    except:
        toadd={"ID": ID, "Password": P, "Fname": FN, "Lname": LN, "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 0}
        database.child("Users").child(ID).set(toadd)
        
def Action():
             global ID
             a=input("Choose Game: 1to9")

             # Beyond this everything in method must be in each game
             score=0
             setgame(a)
             while True:
                 useropt=input("Press w to increase, x to exit")
                 if useropt=='w':
                     score=score+1
                 elif useropt=='x':
                    print("Your Score is: ",score)
                    checkscore(score)
                    break
          
while True:
    print("Welcome to Chemsim")
    ab=input("1) Login, 2) Signup")
    if ab=='1':
        Login()
    elif ab=='2':
        SignUp()




