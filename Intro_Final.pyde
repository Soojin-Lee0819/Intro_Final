from Instruction import *
import os,random
path = os.getcwd() + "/"

#initialize windowsize
RESOLUTION_W = 800
RESOLUTION_H = 900

#button positions
Button_W = RESOLUTION_W/6
Button_H = RESOLUTION_W/10
Button_X = RESOLUTION_W/2 - Button_W/2
Button_Y = RESOLUTION_H/1.75

# instruction page
landingpage = True 
pagetwoText = False
pagethreeText = False

#game page 
onepage = False
twopage = False
threepage = False

# end page either win or loose 
endpage = False
winpage = False

#All About Level 1 
class Person():
    
    def __init__(self, y,img):
    self.y = y
    self.w = 200
    self.h = 200
    self.r = self.w/4
    self.img = loadImage(path + "/images/"+img)
    
    def catch(self):
        for i in range(len(level1.item)-1, -1, -1):
            if self.distance(level1.item[i]) < self.r + level1.item[i].r:
            
                item_caught = level1.item.pop(i)
                    
                if item_caught.rand_index in level1.legend.legend_index:
                    print(type(item_caught.rand_index))
                    loose = level1.legend.remove_item(item_caught.rand_index)
                    return(loose)
                    
                else:
                    loose = 1
                    return(loose)
        
    def distance(self, other):
        return ((mouseX - other.x)**2 + (self.y - other.y)**2)**0.5
        
    def display(self):
        loose = self.catch()
        imageMode(CENTER)
        image(self.img, mouseX, self.y, self.w, self.h)
    
        return(loose)
        
        
        
    def __init__(self, y, img):
        Person.__init__(self, y, img)
    
    def catch(self):
        for i in range(len(level1.item0)-1, -1, -1):
                if self.distance(level1.item0[i]) < self.r + level1.item0[i].r:
                    item_caught = level1.item0.pop(i)
                
                    if item_caught.rand_index in level1.legend.legend_index:
                        loose = level1.legend.remove_item(item_caught.rand_index)
                        return (loose)
                    else:
                        loose = 1
                        print("lost")
                        return(loose)

class Texting(Clothes):

    def __init__(self, w, h, r,vy, rand_index):
        self.w = w
        self.h = h
        self.r = r
        self.vy = vy
        self.x = random.randint(50, RESOLUTION_W - 50)
        self.y = 10
        self.rand_index = rand_index
    
        global texts
        texts = []
        for i in range(15):
            texts.append(loadImage(path + "/images/emoji" + str(i) + ".png"))
        
    def update(self):
        self.y += self.vy  
        
    def __str__(self):
        return {self.rand_index}
        

    def display(self):
        self.update()
        
        image(texts[self.rand_index], self.x, self.y, self.w, self.h)
        # noFill()
        # ellipse(self.x, self.y, self.w, self.h)
        

class Level1():
    
    def __init__(self,img):
        self.bkg_img = loadImage(path + "/images/"+img)
        self.person = Person(RESOLUTION_H - 120, "character1.png")
        self.item = []
        self.item.append(Texting(70, 70, 35, 4, random.randint(0, 14)))
        self.legend = Legend(texts, 210, 100, 70, 70, 1, "#9285E1")

    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        loose = self.person.display()
        
        # Iterate backwards through the list so that the clothes will continue to fall
        for i in range(len(self.item)-1, -1, -1):
            self.item[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.item[i].y > height + self.item[i].r:
                self.item.pop(i)
                        
        # Add new texts item for every 100th or 60th frame
        if frameCount % 100 == 0:
            self.item.append(Texting(70, 70, 35, 4, random.randint(0, 14)))
        elif frameCount % 60 == 0:
            self.item.append(Texting(70, 70, 35, 4, random.randint(0, 14)))
        
        self.legend.display()
        
        return(loose) 
    
    
   
                   


#LEVEL 3 GAME PAGE
class Person3(Person):
    def __init__(self,y, img):
        Person.__init__(self,y,img)
    def catch(self):
        for i in range(len(level3.item2)-1, -1, -1):
            if self.distance(level3.item2[i]) < self.r + level3.item2[i].r:
               
                item_caught = level3.item2.pop(i)
                    
                if item_caught.rand_index in level3.legend.legend_index:
                    print(type(item_caught.rand_index))
                    loose = level3.legend.remove_item(item_caught.rand_index)
                    return(loose)
                    
                else:
                    loose = 1
                    return(loose)

class Food(Clothes):
    def __init__(self, w, h, r, vy, rand_index):
        Clothes.__init__(self, w, h, r, vy, rand_index)
        
        global foods
        foods = []
        
        for i in range(15):
            foods.append(loadImage(path + "/images/food" + str(i) + ".png"))
                         
    def display(self):
        self.update()
        
        image(foods[self.rand_index], self.x, self.y, self.w, self.h)


# All About Level 2 
class Person2(Person):
    
    def __init__(self, y, img):
        Person.__init__(self, y, img)
    
    def catch(self):
        for i in range(len(level2.item0)-1, -1, -1):
                if self.distance(level2.item0[i]) < self.r + level2.item0[i].r:
                    item_caught = level2.item0.pop(i)
                
                    if item_caught.rand_index in level2.legend.legend_index:
                        loose = level2.legend.remove_item(item_caught.rand_index)
                        return (loose)
                    else:
                        loose = 1
                        print("lost")
                        return(loose)

class Clothes(Texting):
    def __init__(self, w, h, r, vy, rand_index):
        Clothes.__init__(self, w, h, r, vy, rand_index)
        
        global texts
        texts = []
        
        for i in range(15):
            texts.append(loadImage(path + "/images/emoji" + str(i) + ".png"))
                         
    def display(self):
        self.update()
        image(texts[self.rand_index], self.x, self.y, self.w, self.h)

class Legend():
    def __init__(self, img, legend_x, legend_y, w, h, level_number, c):    
       
        self.rand_item0 = random.randint(0,2)
        self.rand_item1 = random.randint(3, 5)
        self.rand_item2 = random.randint(6, 8)
        self.rand_item3 = random.randint(9, 11)
        self.rand_item4 = random.randint(12, 14)
        
       
        self.img = img
        self.legend = [self.img[self.rand_item0], self.img[self.rand_item1], self.img[self.rand_item2], self.img[self.rand_item3], self.img[self.rand_item4]]
        self.legend_index = [self.rand_item0 , self.rand_item1, self.rand_item2, self.rand_item3, self.rand_item4]
        self.legend_x = legend_x
        self.legend_y = legend_y
        self.w = w
        self.h = h
        self.level_number = level_number
        self.legend_color = c
        
    def remove_item(self, indexItem):
        item_index = self.legend_index.index(indexItem)
       
        self.legend.pop(item_index)
        self.legend_index.pop(item_index)
        
        if len(self.legend) == 0:
            loose = 2
            return (loose)
        
    def display(self):
        noStroke()
        fill(self.legend_color)
        rect(0, 0, width, 160)
        
        fill(0)
        textSize(30)
        text("LEVEL " + str(self.level_number), 70, 50)

        # Progress Bar/legend
        for i in range(len(self.legend)):
            image(self.legend[i], self.legend_x + (i*100), self.legend_y, self.w, self.h)

       
class Level2(Level1):
     def __init__(self, img):
        Level1.__init__(self, img)
        # self.bkg_img = loadImage(path + "/images/" + img)
        self.person = Person2(RESOLUTION_H - 120, "character1.png")
        self.item0 = []
        self.item0.append(Clothes(70, 70, 35, 5, random.randint(0, 14)))
        self.legend = Legend(clothes, 210, 100, 70, 70, 2, "#da7344")
        
        
    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        loose = self.person.display()
        
        # Iterate backwards through the list so that the clothes will continue to fall
        for i in range(len(self.item0)-1, -1, -1):
            self.item0[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.item0[i].y > height + self.item0[i].r:
                self.item0.pop(i)
                        
        # Add new clothes item for every 100th or 60th frame
        if frameCount % 100 == 0:
            self.item0.append(Clothes(70, 70, 35, 5, random.randint(0, 14)))
                
        elif frameCount % 60 == 0:
            self.item0.append(Clothes(70, 70, 35, 5, random.randint(0, 14)))
        
        self.legend.display()
        return(loose) 
            

class Level3(Level1):
    def __init__(self, img):
        Level2.__init__(self, img)
        # self.bkg_img = loadImage(path + "/images/" + img)
        self.person = Person3(RESOLUTION_H - 120, "character2.png")
        self.item2 = []
        self.item2.append(Food(70, 70, 35, 7, random.randint(0, 14)))
        self.legend = Legend(foods, 210, 100, 70, 70, 3, "#9285E1")
        
        
    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        loose = self.person.display()
        
        # Iterate backwards through the list so that the clothes will continue to fall
        for i in range(len(self.item2)-1, -1, -1):
            self.item2[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.item2[i].y > height + self.item2[i].r:
                self.item2.pop(i)
                        
        # Add new clothes item for every 100th or 60th frame
        if frameCount % 100 == 0:
            self.item2.append(Food(70, 70, 35, 7, random.randint(0, 14)))
                
        elif frameCount % 60 == 0:
            self.item2.append(Food(70, 70, 35, 7, random.randint(0, 14)))
        
        self.legend.display() 
        return(loose) 
                   

def setup():
    size(RESOLUTION_W,RESOLUTION_H)
    
def draw():
    global landingpage
    global onepage
    global twopage
    global threepage
    global pagetwoText 
    global pagethreeText
    global winpage
    global endpage
    
    #track and update mouse position 
    update(mouseX, mouseY)
    
    # landingpage by default
    if landingpage is True:
        landpage.display()
        
    #start level1     
    elif onepage is True:
        background(220)
        loose = level1.display()
        
        # if game ended
        if loose == 1:
            print("page one lost")
            onepage = False
            endpage = True
        
        # if passed the game
        elif loose == 2:
            onepage = False
            pagetwoText  = True
    
    elif pagetwoText is True:
        pagetwo.display()
        
    # start level 2 
    elif twopage is True:
        background(220)
        loose = level2.display()
        
        if loose == 1:
            print("page two lost")
            twopage = False
            endpage = True
        
        elif loose == 2:
            twopage = False
            pagethreeText  = True

    elif pagethreeText is True:
        pagethree.display()
        
    # start level 3 
    elif threepage is True:
        background(220)
        loose = level3.display()
        
        if loose == 1:
            print("page three lost")
            threepage = False
            endpage = True
        
        elif loose == 2:
            threepage = False
            winpage  = True
   

    elif endpage is True:
        loosepage.display()
        
    elif winpage is True:
        winpg.display()


def update(x, y):
    global buttonPressed
    if (overButton(Button_X,Button_Y,Button_W,Button_H)):
        buttonPressed = True
    else:
        buttonPressed = False

def mousePressed():  #If mouse is clicked, then restart the game
    global landingpage
    global onepage
    global twopage
    global threepage
    global pagetwoText 
    global pagethreeText
    global winpage
    global endpage
    
    global level1
    global level2 
    global level3 

    if landingpage is True and buttonPressed is True:
        landingpage = False
        onepage = True
        level1 = Level1("bedroom.jpg")  
        
    elif pagetwoText is True and buttonPressed is True:
        pagetwoText = False
        twopage = True
        level2 = Level2("closet.jpg") 

    elif pagethreeText is True and buttonPressed is True:
       pagethreeText = False
       threepage = True
       level3 = Level3("restaurant.jpg") 

    elif endpage is True and buttonPressed is True:
       endpage = False
       landingpage = True

    elif winpage is True and buttonPressed is True:
       winpage = False
       landingpage = True
          
def overButton(x, y, w, h):
  if (mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h):
    return True
  else:
    return False
