from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboards(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y = 270)
        self.update_scoreboad()
    
    def update_scoreboad(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)

    def add_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboad()

