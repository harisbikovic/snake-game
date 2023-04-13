from turtle import Screen, Turtle
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.turtles_list = []
        self.create_snake()
        self.head = self.turtles_list[0]

    def create_snake(self):
        for n in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            #turtle.shapesize(1.0, 1.0)
            turtle.setposition(n*(-20), 0)
            self.turtles_list.append(turtle)

    def move(self):
        for turtle_num in range(len(self.turtles_list)-1, 0, -1):
            new_x_position = self.turtles_list[turtle_num-1].xcor()
            new_y_position = self.turtles_list[turtle_num-1].ycor()
            self.turtles_list[turtle_num].goto(new_x_position, new_y_position)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        # Snake is moving to the right
        if self.head.xcor() > self.turtles_list[1].xcor():
            self.head.left(90)
        #Snake is moving to the left
        if self.head.xcor() < self.turtles_list[1].xcor():
            self.head.right(90)

    def down(self):
        # Snake is moving to the right
        if self.head.xcor() > self.turtles_list[1].xcor():
            self.head.right(90)
        # Snake is moving to the left
        if self.head.xcor() < self.turtles_list[1].xcor():
            self.head.left(90)

    def left(self):
        # Snake is moving upwards
        if self.head.ycor() > self.turtles_list[1].ycor():
            self.head.left(90)
        # Snake is moving downwards
        if self.head.ycor() < self.turtles_list[1].ycor():
            self.head.right(90)

    def right(self):
        # Snake is moving upwards
        if self.head.ycor() > self.turtles_list[1].ycor():
            self.head.right(90)
        # Snake is moving downwards
        if self.head.ycor() < self.turtles_list[1].ycor():
            self.head.left(90)

    def extend(self):
        self.add_segment(self.turtles_list[-1].position())    # Get the last segment's position and add new one there

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        # turtle.shapesize(1.0, 1.0)
        turtle.setposition(position)
        self.turtles_list.append(turtle)

    def reset(self):
        for turtle in self.turtles_list:
            turtle.goto(1000, 1000)   # Go outside the screen. Otherwise, snake segments stay onscreen
        self.turtles_list.clear()    # Deletes all the turtles from the list (snake vanishes from memory)
        self.create_snake()    # Initialize snake again
        self.head = self.turtles_list[0]