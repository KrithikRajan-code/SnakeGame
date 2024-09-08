STARTING_POSITION= [(0 , 0),(-20,0),(-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
from turtle import Turtle

class Snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head=self.segements[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segemnt(position)
    def add_segemnt(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segements.append(new_turtle)
    def extend(self):
        self.add_segemnt(self.segements[-1].position())

    def move(self):
        for seg_num in range(len(self.segements) - 1, 0, -1):
            new_x = self.segements[seg_num - 1].xcor()
            new_y = self.segements[seg_num - 1].ycor()
            self.segements[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)
    def snake_reset(self):
        for seg in self.segements:
            seg.goto(1080,1080)
        self.segements.clear()
        self.create_snake()
        self.head = self.segements[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


