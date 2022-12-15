import os, random

path = os.getcwd()

RESOLUTION_W = 800
RESOLUTION_H = 900

class Person():
    def __init__(self, y):
        self.y = y
        self.w = 200
        self.h = 200
        self.r = self.w/2
        self.img = loadImage(path + "/images/character.png")
        
    def catch(self):
        for i in range(len(level2.item)-1, -1, -1):
            if self.distance(level2.item[i]) < self.r + level2.item[i].r:
                # print(item_caught, level2.legend.item)
                #print(level2.item[i].rand_index, level2.legend.legend_index)
                item_caught = level2.item.pop(i)
                
                if item_caught.rand_index in level2.legend.legend_index:
                    print(type(item_caught.rand_index))
                    level2.legend.remove_item(item_caught.rand_index)
                
                else:
                    print("end")
        
    def distance(self, other):
        return ((mouseX - other.x)**2 + (self.y - other.y)**2)**0.5
        
    def display(self):
        self.catch()
        
        imageMode(CENTER)
        image(self.img, mouseX, self.y, self.w, self.h)
        # noFill()
        # stroke(255, 0, 0)
        # strokeWeight(2)
        # ellipse(mouseX, self.y, self.w, self.h)
        
class Clothes():
    def __init__(self, w, h, r, rand_index):
        self.w = w
        self.h = h
        self.r = r
        self.x = random.randint(50, RESOLUTION_W - 50)
        self.y = 10
        self.vy = random.randint(4, 10)
        self.rand_index = rand_index
    
        global clothes
        clothes = []
        for i in range(15):
            clothes.append(loadImage(path + "/images/clothes" + str(i) + ".png"))
        
    def update(self):
        self.y += self.vy  
        
    def __str__(self):
        return {self.rand_index}
        
    # def __eq__(self, other):
        # for i in range(len(level2.item)-1, -1, -1):
        #     return self.clothes[i] == other.clothes  
        
    def display(self):
        self.update()
        
        image(clothes[self.rand_index], self.x, self.y, self.w, self.h)
        # noFill()
        # ellipse(self.x, self.y, self.w, self.h)
        

class Legend():
    def __init__(self, legend_x, legend_y, w, h, level_number, c):
        # self.item = []
        # for i in range(15):
        #     self.item.append(loadImage(path + "/images/clothes" + str(i) + ".png")) # Might have to append different items based on level (use if?)
            
        # possibility for items in legend
        # since there are 5 different items and 3 of each in the list of all the items, this will randomly pick and display
        self.rand_item0 = random.randint(0,2)
        self.rand_item1 = random.randint(3, 5)
        self.rand_item2 = random.randint(6, 8)
        self.rand_item3 = random.randint(9, 11)
        self.rand_item4 = random.randint(12, 14)
        
        # Legend variables
        self.legend = [clothes[self.rand_item0], clothes[self.rand_item1], clothes[self.rand_item2], clothes[self.rand_item3], clothes[self.rand_item4]]
        self.legend_index = [self.rand_item0, self.rand_item1, self.rand_item2, self.rand_item3, self.rand_item4]
        self.legend_x = legend_x
        self.legend_y = legend_y
        self.w = w
        self.h = h
        self.level_number = level_number
        self.legend_color = c

    def __eq__(self, other):
        for item in self.legend:
            return item == other.item
        
    def remove_item(self, indexItem):
        item_index = self.legend_index.index(indexItem)
        self.legend.pop(item_index)
        self.legend_index.pop(item_index)
        print("item reexmoved")
        print(self.legend_index)
        print(self.legend)
        
                
        if len(self.legend) is 0:
            print("win")

        
    def display(self):
        noStroke()
        fill(self.legend_color)
        rect(0, 0, width, 160)
        
        fill(0)
        textSize(30)
        text("LEVEL " + str(self.level_number), 20, 50)
        
        # # Legend box
        # strokeWeight(2)
        # stroke(150)
        # fill(255)
        # rect(500, 30, 250, 170, 20)
        
        # # Display the images for the legend
        # image(self.legend[0], self.legend_x, self.legend_y, self.w, self.h)
        # image(self.legend[1], self.legend_x+80, self.legend_y, self.w, self.h)
        # image(self.legend[2], self.legend_x+160, self.legend_y, self.w, self.h)
        # image(self.legend[3], self.legend_x, self.legend_y+70, self.w, self.h)
        # image(self.legend[4], self.legend_x+80, self.legend_y+70, self.w, self.h)
        
        # Progress Bar/legend
        for i in range(len(self.legend)):
            image(self.legend[i], self.legend_x + (i*100), self.legend_y, self.w, self.h)
        
class Level2():
    def __init__(self):
        self.bkg_img = loadImage(path + "/images/closet.jpg")
        self.person = Person(RESOLUTION_H - 120)
        self.item = []
        self.item.append(Clothes(70, 70, 35, random.randint(0, 14)))
        self.legend = Legend(210, 100, 70, 70, 2, "#da7344")

    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        self.person.display()
        
        # Iterate backwards through the list so that the clothes will continue to fall
        for i in range(len(self.item)-1, -1, -1):
            self.item[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.item[i].y > height + self.item[i].r:
                self.item.pop(i)
                        
        # Add new clothes item for every 100th or 60th frame
        if frameCount % 100 == 0:
            self.item.append(Clothes(70, 70, 35, random.randint(0, 14)))
        elif frameCount % 60 == 0:
            self.item.append(Clothes(70, 70, 35, random.randint(0, 14)))
        
        self.legend.display()

def setup():
    size(RESOLUTION_W, RESOLUTION_H)

level2 = Level2()

def draw():
    background(220)
     
    level2.display()
