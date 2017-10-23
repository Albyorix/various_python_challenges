
class Player:
    def __init__(self, position_x, position_y, height, width):
        self.position_x = position_x
        self.position_y = position_y
        self.height = height
        self.width = width
        self.color = 'white'
        self.reset_image()
    def reset_image(self):
        self.image = (self.position_x-self.width/2,self.position_y-self.height/2,self.position_x+self.width/2,self.position_y+self.height/2)


class Element:

    def __init__(self, position_x, position_y, speed_x, speed_y, size):
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.reset_image()

    def reset_image(self):
        self.image = (self.position_x-self.size/2,self.position_y-self.size/2,self.position_x+self.size/2,self.position_y+self.size/2)

class Food(Element):
    def __init__(self, position_x, position_y, speed_x, speed_y, size):
        Element.__init__(self, position_x, position_y, speed_x, speed_y, size)
        self.color = 'white'

class Enemy(Element):
    def __init__(self, position_x, position_y, speed_x, speed_y, size):
        Element.__init__(self, position_x, position_y, speed_x, speed_y, size)
        self.color = 'green'

