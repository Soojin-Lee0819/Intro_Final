import os,random

path = os.getcwd() + "/"
RESOLUTION_W = 800
RESOLUTION_H = 900
gamePage = False

#start button positions
Button_W = RESOLUTION_W/6
Button_H = RESOLUTION_W/10
Button_X = RESOLUTION_W/2 - Button_W/2
Button_Y = RESOLUTION_H/1.75

landingpage = True
onepage = False
twopage = False
winpg = False
loosepg = False

class Landpage():
    def __init__(self):
        self.bgImage = loadImage(path+"images/bgimg.jpg")
        self.header = "Welcome To Date Night!"
        self.content = "You have a crush\n Let's ask them out on a date.\n \n Challenge 1: Pick Up Line\n Collect all items in the index \n and avoid the rest! "
        self.button = "Start"
    def display(self):
        image(self.bgImage, 0,0,RESOLUTION_W ,RESOLUTION_H)
        noStroke()
        fill(255, 255, 255, 225)
        #background 
        rect(RESOLUTION_W/4,RESOLUTION_H/4,RESOLUTION_W/2,RESOLUTION_H/2)
        #textbox
        fill(0)
        textAlign(CENTER)
        textSize(23)
        text(self.header, 400, 300)
        textSize(17)
        text(self.content, 395, 350)
        #button + Start Text
        rect(Button_X,Button_Y,Button_W,Button_H)
        textSize(25)
        fill(255)
        text(self.button, 400,560)
        

class afterOnePage(Landpage):
    def __init__(self,):
        self.bgImage = loadImage(path+"images/afterone.jpg")
        self.header = "Wear Cute Outfit"
        self.content = "Congratulations!\n You completed challenge 1\n \n Challenge 2: Wear cute outfit\n Collect all items in the index \n and avoid the rest! "
        self.button = "Start"
        
class afterTwoPage(Landpage):
    def __init__(self,):
        self.bgImage = loadImage(path+"images/aftertwo.jpg")
        self.header = "Fine Dining"
        self.content = "Congratulations!\n You completed challenge 2\n \n Challenge 3: Fine Dining\n Collect all items in the index \n and avoid the rest! "
        self.button = "Start"
        
class winPage(Landpage):
    def __init__(self,):
        self.bgImage = loadImage(path+"images/win.jpg")
        self.header = "You Won"
        self.content = "Congratulations!\n The Date was Successful!\n \n Maybe a second date?\n Schedule a second date\n and good luck! "
        self.button = "Again"
        
class loosePage(Landpage):
    def __init__(self,):
        self.bgImage = loadImage(path+"images/loose.jpg")
        self.header = "You Lost"
        self.content = "I am sorry :-( \n It didn't go well \n \n Don't be sad \n There is always a 2nd chance! \n Try again. "
        self.button = "Restart"
    
landpage = Landpage()
afterone = afterOnePage()
aftertwo = afterTwoPage()
winpage = winPage()
loosepage = loosePage()


def setup():
    size(RESOLUTION_W,RESOLUTION_H)
    
def draw():
    update(mouseX, mouseY)
    if landingpage is True:
        loosepage.display()
        

        
def update(x, y):
    global buttonPressed
    if (overButton(Button_X,Button_Y,Button_W,Button_H)):
        buttonPressed = True
    else:
        buttonPressed = False

def mousePressed():  #If mouse is clicked, then restart the game
    if buttonPressed == True:
        print("move to level 1")
    else:
        print("game page")
          
def overButton(x, y, w, h):
  if (mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h):
    return True
  else:
    return False
