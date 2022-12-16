import os
path = os.getcwd() + "/"

#initialize windowsize
RESOLUTION_W = 800
RESOLUTION_H = 900

#button positions
Button_W = RESOLUTION_W/6
Button_H = RESOLUTION_W/10
Button_X = RESOLUTION_W/2 - Button_W/2
Button_Y = RESOLUTION_H/1.75

class Landpage():
    def __init__(self):
        self.bgImage = loadImage(path+"images/bgimg.jpg")
        self.header = "Welcome To Date Night!"
        self.content = "You have a crush\n Let's ask them out on a date.\n \n Challenge 1: Pick Up Line\n Use MOUSE to move. Collect items\n in the legend and avoid the rest! "
        self.button = "Start"
    def display(self):
        imageMode(CORNERS)
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
        self.content = "Congratulations!\n You completed challenge 1\n \n Challenge 2: Wear cute outfit\n Use MOUSE to move. Collect items\n in the legend and avoid the rest! "
        self.button = "Start"
        
class afterTwoPage(Landpage):
    def __init__(self):
        self.bgImage = loadImage(path+"images/aftertwo.jpg")
        self.header = "Fine Dining"
        self.content = "Congratulations!\n You completed challenge 2\n \n Challenge 3: Fine Dining\n Use MOUSE to move. Collect items\n in the legend and avoid the rest! "
        self.button = "Start"
        
class winPage(Landpage):
    def __init__(self):
        self.bgImage = loadImage(path+"images/win.jpg")
        self.header = "You Won"
        self.content = "Congratulations!\n The Date was Successful!\n \n Maybe a second date?\n Schedule a second date\n and good luck! "
        self.button = "Again"
        
class losePage(Landpage):
    def __init__(self):
        self.bgImage = loadImage(path+"images/loose.jpg")
        self.header = "You Lost"
        self.content = "I am sorry :-( \n It didn't go well \n \n Don't be sad \n There is always a 2nd chance! \n Try again. "
        self.button = "Restart"

landpage = Landpage()
pagetwo = afterOnePage()
pagethree = afterTwoPage()
winpg = winPage()
losepage = losePage()
