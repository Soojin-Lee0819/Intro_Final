from const import *

class Person():
    def __init__(self, y):
        self.y = y
        self.w = 200
        self.h = 200
        self.r = self.w/2
        self.img = loadImage(path + "/images/character.png")
        
    def catch(self):
        for i in range(len(level2.falling_clothes)-1, -1, -1):
            if self.distance(level2.falling_clothes[i]) < self.r + level2.falling_clothes[i].r:
                item_caught = level2.falling_clothes.pop(i) # everything but the character and background disappears when it is caught
                # print(item_caught)
                
                # if item_caught == Level2()().falling_clothes[i]:
                #     failling_clothes.legend.pop(i)
        
    def distance(self, other):
        return ((mouseX - other.x)**2 + (self.y - other.y)**2)**0.5
    
    # def __eq__(self, other):
        # return
        
    def display(self):
        self.catch()
        
        imageMode(CENTER)
        image(self.img, mouseX, self.y, self.w, self.h)
        # noFill()
        # stroke(255, 0, 0)
        # strokeWeight(2)
        # ellipse(mouseX, self.y, self.w, self.h)
        
class Clothes():
    def __init__(self, w, h, r):
        self.w = w
        self.h = h
        self.r = r
        self.x = random.randint(50, RESOLUTION_W - 50)
        self.y = 10
        self.vy = random.randint(4, 10)
        self.rand_index = random.randint(0, 14)
        self.rand_hat = random.randint(0,2)
        self.rand_jacket = random.randint(3, 5)
        self.rand_pant = random.randint(6, 8)
        self.rand_shoe = random.randint(9, 11)
        self.rand_shirt = random.randint(11, 14)
        
    
        self.clothes = []
        for i in range(15):
            self.clothes.append(loadImage(path + "/images/clothes" + str(i) + ".png"))
        
        # Randomizes again after catching an item :(( I tried moving the legend to the game class but it didn't really work
        self.legend = [self.clothes[self.rand_hat], self.clothes[self.rand_jacket], self.clothes[self.rand_pant], self.clothes[self.rand_shoe], self.clothes[self.rand_shirt]]
        
    def update(self):
        self.y += self.vy  
        
    # We have to somehow figure out how to compare the object caught with the legend image. I was thinking of using __eq__ since it's comparing the instance of the object, but idk if this will work
    def __eq__(self, other):
        for i in range(len(level2.falling_clothes)-1, -1, -1):
            return self.clothes[i] == level2.falling_clothes[i]   
        
    def display(self):
        self.update()
        
        image(self.clothes[self.rand_index], self.x, self.y, self.w, self.h)
        # noFill()
        # ellipse(self.x, self.y, self.w, self.h)
        
        # Create Legend
        noStroke()
        fill(255, 0, 0)
        rect(0, 0, width, 120)
        
        # Legend box
        strokeWeight(2)
        stroke(150)
        fill(255)
        rect(500, 30, 250, 170, 20)
        
        image(self.legend[0], 540, 80, self.w, self.h)
        image(self.legend[1], 620, 80, self.w, self.h)
        image(self.legend[2], 700, 80, self.w, self.h)
        image(self.legend[3], 540, 150, self.w, self.h)
        image(self.legend[4], 620, 150, self.w, self.h)

        
        
class Level2():
    def __init__(self):
        self.bkg_img = loadImage(path + "/images/closet.jpg")
        self.person = Person(RESOLUTION_H - 120)
        self.falling_clothes = []
        self.falling_clothes.append(Clothes(70, 70, 35))

    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        self.person.display()
        
        for i in range(len(self.falling_clothes)-1, -1, -1):
            self.falling_clothes[i].display()
            
            if self.falling_clothes[i].y > height + self.falling_clothes[i].r:
                self.falling_clothes.pop(i)
                print(len(self.falling_clothes))
        
        if frameCount % 100 == 0:
            self.falling_clothes.append(Clothes(70, 70, 35))
            
level2 = Level2()
