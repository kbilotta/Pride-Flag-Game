"""A game about pride flags. :)"""
#python -m hack.hackathon


from turtle import Turtle, bgcolor, update, done, onkey, listen
from typing import Dict
import random


t1: Turtle = Turtle()
correct: Turtle = Turtle()
incorrect: Turtle = Turtle()
n_duck: Turtle = Turtle()


def main() -> None:
    """This bad boy can fit a whole lot of code B) (entrypoint to program)"""
    bgcolor("mistyrose")
    q1()
    #q_function_list = [q1]
    #put all question functions in this list so that I can randomly access them
    #for q in range(10):
        #random.choice(q_function_list)
    done()  

def select_answer() -> None:
    correct.write("That's correct!")

def select_incorrect() -> None:
    incorrect.write("Sorry, that's not correct.")


def q1() -> None:
    """What flag -> trans."""
    t1.hideturtle()
    t1.penup()
    t1.left(90)
    t1.forward(180)
    t1.left(90)
    t1.forward(235)
    t1.pendown()
    t1.pencolor("lightcoral")
    t1.write("What community does this flag represent?", move=False, align="left", font=("Century Gothic", 17, "bold"))
    t1.penup()
    t1.left(90)
    t1.forward(400)
    t1.pendown()
    t1.write("Trans", move=False, align="left", font=("Century Gothic", 17, "bold"))
    t1.penup()
    t1.left(90)
    t1.forward(175)
    t1.pendown()
    t1.write("Bisexual", move=False, align="left", font=("Century Gothic", 17, "bold"))
    t1.penup()
    t1.forward(175)
    t1.pendown()
    t1.write("Pansexual", move=False, align="left", font=("Century Gothic", 17, "bold"))

    onkey(select_answer, "a")
    onkey(select_incorrect, "s")
    onkey(select_incorrect, "d")
    listen()

    
def neutral_duck_sprite() -> None:
    n_duck.penup()
    n_duck.pencolor("yellow")

if __name__ == "__main__":
    main()

