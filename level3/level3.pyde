class Food(Clothes):
    def __init__(self, w, h, r, vy, rand_index):
        Clothes.__init__(w, h, r, vy, rand_index)
        
        global foods
        foods = []
        
        for i in range(15):
            foods.append(loadImage(path + "/images/food" + str(i) + ".png")
                         
    def display():
        self.update()
        
        image(foods[self.rand_index], self.x, self.y, self.w, self.h)

class Level3(Level2):
    def __init__(self):
        Level2.__init__(self, img)
        # self.bkg_img = loadImage(path + "/images/" + img)
        self.person = Person(RESOLUTION_H - 120, "character2.png")
        self.item2 = []
        self.item2.append(Foods(70, 70, 35, random.randint(5, 10), random.randint(0, 14)))
        self.legend(210, 100, 70, 70, 3, "#9285E1")
        
        
    def display(self):
        push()
        tint(255, 70)
        image(self.bkg_img, width/2, height/2, 1200, 900)
        pop()
        self.person.display()
        
        # Iterate backwards through the list so that the clothes will continue to fall
        for i in range(len(self.item)-1, -1, -1):
            self.item2[i].display()
            
            # Make sure to remove any items in the list that were not caught so that the list doesn't continue growing
            if self.item2[i].y > height + self.item[i].r:
                self.item2.pop(i)
                        
        # Add new clothes item for every 100th or 60th frame
        # new_item = Clothes(70, 70, 35, random.randint(4, 10), random.randint(0, 14))
        if frameCount % 100 == 0:
            # while self.check_overlap(new_item) == False:
            #      new_item = Clothes(70, 70, 35, random.randint(4, 10), random.randint(0, 14))
            # self.item.append(new_item)
            # for i in range(len(self.item)-1, -1, -1):
            #     self.store_item_x.append(self.item[i].x)
            self.item2.append(Food(70, 70, 35, random.randint(4, 10), random.randint(0, 14)))
                
        elif frameCount % 60 == 0:
            self.item2.append(Food(70, 70, 35, random.randint(4, 10), random.randint(0, 14)))
        
        self.legend.display()            
