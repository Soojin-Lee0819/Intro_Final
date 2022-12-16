from Instruction import *
import os,random
add_library('minim')

path = os.getcwd() + "/"
player = Minim(this)

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

# end page either win or lose 
endpage = False
winpage = False

#bring sound file
lose_sound = player.loadFile(path + "/sounds/lose_sound.mp3")
bkg_sound = player.loadFile(path + "/sounds/bkg_sound.mp3")
win_sound = player.loadFile(path + "/sounds/win_sound.mp3")
catch_sound = player.loadFile(path + "/sounds/catch_sound.mp3")

# This class creates the legend with the items needed to be collected in each level
# Each level class calls the legend with a different argument for the img, level_number, and color
class Legend():
    
    def __init__(self, img, legend_x, legend_y, w, h, level_number, c):    
        
        # There 5 images being displayed in the legend but 3 possible images in each of the 5.
        # So we sectioned it and created random numbers for each of the 5 to ensure there's no overlapping images in the legend
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
        
    # This method removes the item from the legend so the player can see their progress in the game
    # It also removes it from the legend_index, which we use to check if the item caught is the same as the legend
    def remove_item(self, item):
        # Since legend index is not the same as the list of items falling down, we use .index to find the element in the legend
        item_index = self.legend_index.index(item)
       
        # Then we use that number to pop the element in the legend and legend index
        self.legend.pop(item_index)
        self.legend_index.pop(item_index)
        
        # If the length of the legend list is 0, we move onto the next level b/c the player completed that level
        if len(self.legend) == 0:
            lose = 2
            return (lose)
        
    def display(self):
        noStroke()
        fill(self.legend_color)
        rect(0, 0, width, 160)
        
        fill(0)
        textSize(30)
        text("LEVEL " + str(self.level_number), 70, 50)
        push()
        fill(30)
        textSize(15)
        text("| Collect Items In Any Order", 270, 50)
        pop()

        # Progress Bar/legend
        for i in range(len(self.legend)): # Make sure to use len(self.legend) so 
            image(self.legend[i], self.legend_x + (i*100), self.legend_y, self.w, self.h)


# The next three classes are used for level 1: 
# 1) Person class is for the character on the screen that catches the items falling down 
# 2) Texting class creates one of the items falling on the screen
# 3) Level class creates the object for Person and Texting and is in charge of displaying the overall mechanics of level 1, such as multiple items falling
class Person():
    
    def __init__(self, y,img):
        self.y = y
        self.w = 200
        self.h = 200
        self.r = self.w/4
        self.img = loadImage(path + "/images/"+img)
    
    # This method is used to catch any item falling on the screen
    def catch(self):
        
        # For loop goes backwards since we're popping elements out of the list
        for i in range(len(level1.texts)-1, -1, -1):
            # Checks if the distance is less than the radius of the item and character
            if self.distance(level1.texts[i]) < self.r + level1.texts[i].r:
                item_caught = level1.texts.pop(i) 
                    
                # If the index of the item caught matches the index of the legend item, it plays a sound and goes to the method in the legend
                if item_caught.rand_index in level1.legend.legend_index:
                    catch_sound.rewind()
                    catch_sound.play()
                    lose = level1.legend.remove_item(item_caught.rand_index)
                    return lose
               
                # If the item caught is not in the legend, you lose 
                else:
                    lose = 1
                    return lose
     
     # Used to check the distance between the character's x (which follows the mouse X position) and other which is the item's x
     # Distance formula 
    def distance(self, other):
        return ((mouseX - other.x)**2 + (self.y - other.y)**2)**0.5
        
    def display(self):
        lose = self.catch()
        imageMode(CENTER)
        image(self.img, mouseX, self.y, self.w, self.h)
    
        return lose

# Class for the item falling in level 1 (emojis)
class Texting():

    def __init__(self, w, h, r,vy, rand_index):
        self.w = w
        self.h = h
        self.r = r
        self.vy = vy
        self.x = random.randrange(50, RESOLUTION_W - 50, 80) # Used randrange instead of randint so it's more uniform when falling
        self.y = 10
        self.rand_index = rand_index
    
        # Globalized texts so legend is sharing the same list; makes it easier for checking if the item caught is the same as the item in the legend
        global texts
        texts = []
        for i in range(15):
            texts.append(loadImage(path + "/images/emoji" + str(i) + ".png"))
        
    def update(self):
        self.y += self.vy  

    def display(self):
        self.update()

        image(texts[self.rand_index], self.x, self.y, self.w, self.h)
        
# Class used to display everything and create instance of the legend and item falling
class Level1():
    def __init__(self,img):
        self.bkg_img = loadImage(path + "/images/"+img)
        self.person = Person(RESOLUTION_H - 120, "character0.png")
        self.texts = []
        self.texts.append(Texting(70, 70, 35, 10, random.randint(0, 14))) # Since it is calling a random index, sometimes multiple of the same one shows up or one doesn't show up for a long time
        self.legend = Legend(texts, 210, 100, 70, 70, 1, "#F57CB6")
        bkg_sound.loop()

    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        lose = self.person.display()
        
        # Again we have to iterate through the list backwards because we are removing elements from it
        for i in range(len(self.texts)-1, -1, -1):
            self.texts[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.texts[i].y > height + self.texts[i].r:
                self.texts.pop(i)
                        
        # Add new texts item for every 39th frame
        if frameCount % 33 == 0:
            self.texts.append(Texting(70, 70, 35, 10, random.randint(0, 14)))

        self.legend.display()
        
        return(lose) 
    
    
# The next three classes relate to level 2
# Person2 inherits from Person. We couldn't use the same person class since we are checking a different level's item 
class Person2(Person):
    
    def __init__(self, y, img):
        Person.__init__(self, y, img)
    
    def catch(self):
        for i in range(len(level2.clothes)-1, -1, -1):
                if self.distance(level2.clothes[i]) < self.r + level2.clothes[i].r:
                    item_caught = level2.clothes.pop(i)
                    catch_sound.rewind()
                    catch_sound.play()
                    
                    if item_caught.rand_index in level2.legend.legend_index:
                        lose = level2.legend.remove_item(item_caught.rand_index)
                        return (lose)
                    else:
                        lose = 1
                        print("lost")
                        return(lose)

# Clothes inherits from Texting, only thing different is the displayed image and the list of items
class Clothes(Texting):
    def __init__(self, w, h, r, vy, rand_index):
        Texting.__init__(self, w, h, r, vy, rand_index)
        
        global clothes
        clothes = []
        for i in range(15):
            clothes.append(loadImage(path + "/images/clothes" + str(i) + ".png"))
                         
    def display(self):
        self.update()
        image(clothes[self.rand_index], self.x, self.y, self.w, self.h)


# Level 2 inherits from Level 1, the display is different as it is showing a different character and items falling
class Level2(Level1):
    def __init__(self, img):
        Level1.__init__(self, img)
        self.person = Person2(RESOLUTION_H - 120, "character1.png")
        self.clothes = []
        self.clothes.append(Clothes(70, 70, 35, 13, random.randint(0, 14))) # increase speed of the items falling (13)
        self.legend = Legend(clothes, 210, 100, 70, 70, 2, "#da7344") # Change the img, level_number, and color argument to match level 2
        
    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        lose = self.person.display()
        
        for i in range(len(self.clothes)-1, -1, -1):
            self.clothes[i].display()
    
            if self.clothes[i].y > height + self.clothes[i].r:
                self.clothes.pop(i)
                        
        # Add new clothes item every 21 frames; changing the frame count makes the items appear more frequently
        if frameCount % 21 == 0:
            self.clothes.append(Clothes(70, 70, 35, 13, random.randint(0, 14)))
        
        self.legend.display()
        return lose
            
# The next three classes relate to Level 3
# It is basically the same cases as level 2, we had to change the list of images and the checking for the item caught
class Person3(Person):
    def __init__(self,y, img):
        Person.__init__(self,y,img)
        
    def catch(self):
        for i in range(len(level3.foods)-1, -1, -1):
            if self.distance(level3.foods[i]) < self.r + level3.foods[i].r:
                item_caught = level3.foods.pop(i)
                    
                if item_caught.rand_index in level3.legend.legend_index:
                    catch_sound.rewind()
                    catch_sound.play()
                    lose = level3.legend.remove_item(item_caught.rand_index)
                    return(lose)
                    
                else:
                    lose = 1
                    return(lose)

class Food(Texting):
    def __init__(self, w, h, r, vy, rand_index):
        Texting.__init__(self, w, h, r, vy, rand_index)
        
        global foods
        foods = []
        for i in range(15):
            foods.append(loadImage(path + "/images/food" + str(i) + ".png"))
                         
    def display(self):
        self.update()
        
        image(foods[self.rand_index], self.x, self.y, self.w, self.h)
        
        
class Level3(Level1):
    def __init__(self, img):
        Level1.__init__(self, img)
        self.person = Person3(RESOLUTION_H - 120, "character2.png")
        self.foods = []
        self.foods.append(Food(70, 70, 35, 15, random.randint(0, 14))) # Also increased the speed 
        self.legend = Legend(foods, 210, 100, 70, 70, 3, "#9285E1")
        
        
    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        lose = self.person.display()
        
        for i in range(len(self.foods)-1, -1, -1):
            self.foods[i].display()
        
            if self.foods[i].y > height + self.foods[i].r:
                self.foods.pop(i)
                        
        # Add new clothes item for every 13 frames
        if frameCount % 13 == 0:
            self.foods.append(Food(70, 70, 35, 15, random.randint(0, 14)))        
        
        self.legend.display() 
        return(lose) 
                   

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
        lose = level1.display()
        
        # if game ended
        if lose == 1:
            print("page one lost")
            onepage = False
            endpage = True
            
        
        # if passed the game
        elif lose == 2:
            onepage = False
            pagetwoText  = True
            
    
    elif pagetwoText is True:
        pagetwo.display()
        bkg_sound.pause()
        bkg_sound.rewind()
        
        
    # start level 2 
    elif twopage is True:
        background(220)
        lose = level2.display()
        
        if lose == 1:
            print("page two lost")
            twopage = False
            endpage = True
        
        elif lose == 2:
            twopage = False
            pagethreeText  = True

    elif pagethreeText is True:
        pagethree.display()
        bkg_sound.pause()
        bkg_sound.rewind()
        
    # start level 3 
    elif threepage is True:
        background(220)
        lose = level3.display()
        
        if lose == 1:
            print("page three lost")
            threepage = False
            endpage = True
        
        elif lose == 2:
            threepage = False
            winpage  = True
   

    elif endpage is True:
        bkg_sound.pause()
        if not lose_sound.isPlaying():
            lose_sound.play()
            
            
        losepage.display()
        
    elif winpage is True:
        bkg_sound.pause()
        if not win_sound.isPlaying():
            win_sound.play()
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
        bkg_sound.rewind()
        win_sound.rewind()
        lose_sound.rewind()
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
       lose_sound.pause()

    elif winpage is True and buttonPressed is True:
       winpage = False
       landingpage = True
       win_sound.pause()
       
          
def overButton(x, y, w, h):
  if (mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h):
    return True
  else:
    return False
