from const import *
from level2 import *


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


class Level3(Level2):
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
        self.person.display()
        
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
                   
level3 = Level3("restaurant.jpg") 
