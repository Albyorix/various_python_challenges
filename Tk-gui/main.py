from Tkinter import *
from random import *
from Agents import *

class Game:

    def __init__(self):
        self.root = Tk()
        self.GAME_WIDTH = 500
        self.GAME_HEIGHT = 500
        self.RUN = False
        self.frame = Frame(bg='black')
        self.frame.pack()
        self.canvas = Canvas(self.frame, bg='black',width=self.GAME_WIDTH,height=self.GAME_HEIGHT)
        self.canvas.pack()
        self.points = Label(self.frame, bg='black', fg='white')
        self.points.pack()
        self.start_button = Button(self.frame, bg='black', fg='white', text='Start', command=self.start)
        self.start_button.pack()
        self.root.mainloop()

    def start(self):
        self.RUN = True
        PLAYER_HEIGHT = 30
        PLAYER_WIDTH = 15
        PLAYER_START_POSITION_Y = 480
        PLAYER_START_POSITION_X = 250
        self.player = Player(PLAYER_START_POSITION_X, PLAYER_START_POSITION_Y, PLAYER_HEIGHT, PLAYER_WIDTH)
        self.elements = []
        self.root.bind("<Key>", self.move_agent)
        self.time = 0
        self.point = 0
        self.time_to_next_food = self.get_time_to_next_element()
        self.time_to_next_enemy = self.get_time_to_next_element()
        self.run()

    def run(self):
        if self.RUN:
            self.paint()
            self.time += 1
            self.point -= 1
            self.time_to_next_food -= 1
            self.time_to_next_enemy -= 1
            self.move_elements()
            if self.time_to_next_food < 0:
                self.create_food()
                self.time_to_next_food = self.get_time_to_next_element()
            if self.time_to_next_enemy < 0:
                self.create_enemy()
                self.time_to_next_enemy = self.get_time_to_next_element()
            self.delete_outside_elements()
            self.root.after(10, self.run)

    def delete_outside_elements(self):
        index_to_delete = []
        for i in range(len(self.elements)-1, 0, -1):
            if not (-self.elements[i].size < self.elements[i].position_y < self.GAME_HEIGHT + self.elements[i].size and
                -self.elements[i].size < self.elements[i].position_x < self.GAME_WIDTH + self.elements[i].size):
                index_to_delete.append(i)
        for i in index_to_delete:
            self.elements.pop(i)

    def get_time_to_next_element(self):
        time = int(random() * 100)
        return time

    def move_agent(self, event):
        speed = 2
        if event.keycode == 38: #UP
            self.player.position_y -= speed
        elif event.keycode == 39: #RIGHT
            self.player.position_x += speed
        elif event.keycode == 40: #DOWN
            self.player.position_y += speed
        elif event.keycode == 37: #LEFT
            self.player.position_x -= speed
        self.player.reset_image()

    def get_random_new_position(self):
        size = 8 + int(random() * 12)
        position_x = int(random() * 500)
        speed_y = random() * 3
        return size, position_x, speed_y

    def create_enemy(self):
        size, position_x, speed_y = self.get_random_new_position()
        self.elements.append(Enemy(position_x, 0, 0, speed_y, size))

    def create_food(self):
        size, position_x, speed_y = self.get_random_new_position()
        self.elements.append(Food(position_x, 0, 0, speed_y, size))

    def move_elements(self):
        for element in self.elements:
            element.position_y += element.speed_y
            element.speed_y += element.size / 1000.
            element.reset_image()

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(self.player.image, fill=self.player.color)
        for element in self.elements:
            self.canvas.create_oval(element.image, fill=element.color)
        self.points['text'] = 'Score = ' + str(int(self.point/10))

app = Game()
in