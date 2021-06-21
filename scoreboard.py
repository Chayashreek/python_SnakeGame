from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score_board()
    def update_score_board(self):
        self.clear()
        self.write(f"Score:{self.score},High Score:{self.high_score}",align="center", font=("Courier", 24, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
    #def game_over(self):
     #   self.goto(0,0)
      #  self.write("OOPS!\nYou hit the wall\nGame over",align="center",font="Courier")

    def tail_game_over(self):
        self.goto(0, 0)
        self.write("OOPS!\nYou have bite ur own tail;)\nGame over", align="center", font="Courier")

    def increase_score(self):
        self.score+=1
        self.update_score_board()