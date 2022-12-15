from const import *
from Instruction import *
from level2 import *
from level3 import *
from level1 import *

landingpage = True
twopage = False
onepage = False
threepage = False
pagethree = False

endpage = False

def setup():
    size(RESOLUTION_W,RESOLUTION_H)
    
def draw():
    global landingpage
    global twopage
    global threepage
    global endpage
    global onepage
    update(mouseX, mouseY)
    if landingpage is True:
        landpage.display()
        
    elif onepage is True:
        background(220)
        loose = level1.display()
        if loose == 1:
            print("page one lost")
            onepage = False
            endpage = True
        
        elif loose == 2:
            onepage = False
            twopage = True
            print("page one win")
            

    elif threepage is True:
        aftertwo.display()
        

    elif endpage is True:
        loosepage.display()


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
    global threepage
    global pagethree
    global winpage
    global endpage

    if landingpage is True and buttonPressed is True:
        landingpage = False
        onepage = True

    elif endpage is True and buttonPressed is True:
       endpage = False
       landingpage = True

    elif threepage is True and buttonPressed is True:
        threepage = False
        pagethree = True
          
def overButton(x, y, w, h):
  if (mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h):
    return True
  else:
    return False
