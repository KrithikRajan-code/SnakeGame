from food import Food

class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as file :
            self.high_score = int(file.read())



    def write_text(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score:{self.score}  High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        self.pendown()
    def again_reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_text()
        with open("data.txt" ,mode="w") as data:
            data.write(f"{self.high_score}")




    def clear_text(self):
        self.clear()  # Clear any existing drawings or text
