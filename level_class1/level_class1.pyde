import os, random

path = os.getcwd()

RESOLUTION_W = 800
RESOLUTION_H = 900

class Person():
    def __init__(self):
        self.y = RESOLUTION_H - 120
        self.w = 200
        self.h = 200
        self.r = self.w/2
        self.img = loadImage(path + "/images/character.png")
        
    # def catch(self):
    #     if self.distance(level1.falling_text) < self.r + level1.falling_text.r:
            
        
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        
    def display(self):
        imageMode(CENTER)
        image(self.img, mouseX, self.y, self.w, self.h)
        noFill()
        stroke(255, 0, 0)
        strokeWeight(2)
        ellipse(mouseX, self.y, self.w, self.h)
        
class Text():
    def __init__(self):
        # self.text_list = ["Are you free on Friday?", "down 2 get dinner 2night?", "Hey, are you feeling hungry?", "Want to go eat tonight?"]
        # self.text_words = ["Are", "you", "free", "on", "Friday?", "Monday?", "Tuesday?", "down", "2", "get", "dinner", "2night?", "tonight?"]
        self.text_list = ["Are", "you", "free", "on", "friday?"]
        self.text_words = ["Are", "you", "free", "on", "Friday?", "Monday?", "r", "u", "Tuesday?", "down", "2", "get", "dinner", "2night?", "tonight?"]
        self.empty_list = []
        self.x = random.randint(50, RESOLUTION_W - 50)
        self.y = -30
        # self.vy = random.randint(2, 10)
        self.vy = random.randint(1,4)
        self.rand_index = random.randint(0, 14)
        
    def update(self):
        self.y += self.vy        
        
    def display(self):
        self.update()
        textSize(20)
        fill(0)
        text(self.text_words[self.rand_index], self.x, self.y)

        noStroke()
        fill(255, 0, 0)
        rect(0, 0, width, 120)
        
        # Legend box
        strokeWeight(2)
        stroke(150)
        fill(255)
        rect(width - 300, 30, 250, 170, 20)
        
class Level1:
    def __init__(self):
        self.person = Person()
        self.falling_text = Text()
    
    def display(self):
        
        self.person.display()
        self.falling_text.display()
        


def setup():
    size(RESOLUTION_W, RESOLUTION_H)

level1 = Level1()

def draw():
    background(220)
    
    level1.display()
    
