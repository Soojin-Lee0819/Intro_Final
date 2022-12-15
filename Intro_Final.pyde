from const import *
from Instruction import *
from level2 import *


landingpage = True



def setup():
    size(RESOLUTION_W,RESOLUTION_H)
    
def draw():
    global landingpage
    update(mouseX, mouseY)
    if landingpage is True:
        landpage.display()
    elif twopage is True:
        background(220)
        level2.display()
 
        

        
def update(x, y):
    global buttonPressed
    if (overButton(Button_X,Button_Y,Button_W,Button_H)):
        buttonPressed = True
    else:
        buttonPressed = False

def mousePressed():  #If mouse is clicked, then restart the game
    global landingpage
    global gamePage
    global onepage
    global twopage
    global winpage
    global loosepg

    if landingpage is True and buttonPressed is True:
        print("move to level 1")
        landingpage = False
        twopage = True

    else:
        print("game page")
          
def overButton(x, y, w, h):
  if (mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h):
    return True
  else:
    return False
