from const import *

class Person():
    def __init__(self, y,img):
        self.y = y
        self.w = 200
        self.h = 200
        self.r = self.w/2
        self.img = loadImage(path + "/images/"+img)
        
    def catch(self):
        for i in range(len(level2.item)-1, -1, -1):
            if self.distance(level2.item[i]) < self.r + level2.item[i].r:
               
                item_caught = level2.item.pop(i)
                    
                if item_caught.rand_index in level2.legend.legend_index:
                    print(type(item_caught.rand_index))
                    loose = level2.legend.remove_item(item_caught.rand_index)
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
        
class Clothes():
    def __init__(self, w, h, r,vy, rand_index):
        self.w = w
        self.h = h
        self.r = r
        self.vy = vy
        self.x = random.randint(50, RESOLUTION_W - 50)
        self.y = 10
        self.rand_index = rand_index
    
        global clothes
        clothes = []
        for i in range(15):
            clothes.append(loadImage(path + "/images/clothes" + str(i) + ".png"))
        
    def update(self):
        self.y += self.vy  
        
    def __str__(self):
        return {self.rand_index}
        

    def display(self):
        self.update()
        
        image(clothes[self.rand_index], self.x, self.y, self.w, self.h)
        # noFill()
        # ellipse(self.x, self.y, self.w, self.h)
        

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

       
class Level2():
    def __init__(self,img):
        self.bkg_img = loadImage(path + "/images/"+img)
        self.person = Person(RESOLUTION_H - 120, "character1.png")
        self.item = []
        self.item.append(Clothes(70, 70, 35, 4, random.randint(0, 14)))
        self.legend = Legend(clothes, 210, 100, 70, 70, 2, "#da7344")

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
                        
        # Add new clothes item for every 100th or 60th frame
        if frameCount % 100 == 0:
            self.item.append(Clothes(70, 70, 35, 4, random.randint(0, 14)))
        elif frameCount % 60 == 0:
            self.item.append(Clothes(70, 70, 35, 4, random.randint(0, 14)))
        
        self.legend.display()
        
        return(loose) 




level2 = Level2("closet.jpg") 
