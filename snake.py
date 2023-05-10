from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-40, 0), (-40, 0), (-40, 0), (-40, 0), (-40, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment((self.segments[-1].position()))

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN and int(self.head.xcor()) != int(self.segments[1].xcor()):
            # print(self.head.xcor(), self.segments[1].xcor())
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and int(self.head.xcor()) != int(self.segments[1].xcor()):
            # print(self.head.xcor(), self.segments[1].xcor())
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT and int(self.head.ycor()) != int(self.segments[1].ycor()):
            # print(self.head.ycor(), self.segments[1].ycor())
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT and int(self.head.ycor()) != int(self.segments[1].ycor()):
            # print(self.head.ycor(), self.segments[1].ycor())
            self.head.setheading(LEFT)
