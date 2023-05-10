import json
from turtle import Turtle

FONT_SCOREBOARD = ('Courier', 10, 'normal')
FONT_GAME_OVER = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.json', "r") as file:
            self.data = json.load(file)
        self.high_score = self.data['high_score']
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}, High score: {self.high_score}', font=FONT_SCOREBOARD, align=ALIGNMENT)

    def reset(self):
        self.goto(0, 280)
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.json', "w") as file:
                self.data['high_score'] = self.high_score
                json_data = json.dumps(self.data, indent=2)
                file.write(json_data)
        self.score = 0
        self.refresh_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over!', font=FONT_GAME_OVER, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

