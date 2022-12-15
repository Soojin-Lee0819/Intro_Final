from const import *
from level2 import *


class Person1(Person):
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
    def __init__(self, w, h, r, vy, rand_index):
        Clothes.__init__(self, w, h, r, vy, rand_index)
        
        global texts
        texts = []
        
        for i in range(15):
            texts.append(loadImage(path + "/images/emoji" + str(i) + ".png"))
                         
    def display(self):
        self.update()
        image(texts[self.rand_index], self.x, self.y, self.w, self.h)

class Level1(Level2):
    def __init__(self, img):
        Level2.__init__(self, img)
        # self.bkg_img = loadImage(path + "/images/" + img)
        self.person = Person1(RESOLUTION_H - 120, "character0.png")
        self.item0 = []
        self.item0.append(Texting(70, 70, 35, 5, random.randint(0, 14)))
        self.legend = Legend(texts, 210, 100, 70, 70, 1, "#F57CB6")
        
        
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
            self.item0.append(Texting(70, 70, 35, 5, random.randint(0, 14)))
                
        elif frameCount % 60 == 0:
            self.item0.append(Texting(70, 70, 35, 5, random.randint(0, 14)))
        
        self.legend.display()
        return(loose) 
                   
