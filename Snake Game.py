# Project Name - Task_3_Snake_Game
# Developed By - Ajay Thakur (2016kuec2026@iiitkota.ac.in)
# Branch Name - Electronics and Communication Engineering
# Institute Name - Indian Institute of Information Technology Kota (An Institute of National Importance under an Act of Parliament)
# Submitted To -  Code Alpha
# Project Link (GitHub) - https://github.com/ajaythakur3369/CodeAlpha-Password-Generator/blob/main/Task_3_Snake_Game.py

# Project Summery - With older Nokia phones, we had an old-age addiction with the snake game. But of course, we don’t have it anymore. So, we built a Project using 
# Python. Beginner Python programmers who are interested in making something easier in their domain can definitely try this out, and the module Turtle was built.

# Importing libraries
import turtle
import time
import random

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width = 600, height = 600)

# Initialize the snake and food
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

segments = []

# Functions to move the snake
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

def check_collision():
    if (
        snake.xcor() > 290
        or snake.xcor() < -290
        or snake.ycor() > 290
        or snake.ycor() < -290
    ):
        return True

    for segment in segments:
        if snake.distance(segment) < 20:
            return True

    return False

def generate_food():
    food.goto(random.randint(-290, 290), random.randint(-290, 290))

def update_score(score):
    score_display.clear()
    score_display.write(f"Score: {score}", align = "center", font = ("Georgia", 24, "normal"))

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Initialize the score
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align = "center", font = ("Georgia", 24, "normal"))

# Main game loop
while True:
    window.update()

    if check_collision():
        snake.goto(0, 0)
        snake.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        update_score(score)

    if snake.distance(food) < 20:
        generate_food()
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        score += 5
        update_score(score)

    # Move the segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collisions with the wall
    if (
        snake.xcor() > 290
        or snake.xcor() < -290
        or snake.ycor() > 290
        or snake.ycor() < -290
    ):
        game_over_text = turtle.Turtle()
        game_over_text.speed(0)
        game_over_text.color("white")
        game_over_text.penup()
        game_over_text.hideturtle()
        game_over_text.goto(0, 0)
        game_over_text.write("Game Over!", align = "center", font = ("Georgia", 24, "normal"))
        time.sleep(2)
        game_over_text.clear()
        snake.goto(0, 0)
        snake.direction = "stop"
        score = 0
        score_display.clear()
        score_display.write("Score: 0", align = "center", font = ("Georgia", 24, "normal"))

    # Check for collisions with the snake's body
    for segment in segments:
        if segment.distance(snake) < 20:
            game_over_text = turtle.Turtle()
            game_over_text.speed(0)
            game_over_text.color("white")
            game_over_text.penup()
            game_over_text.hideturtle()
            game_over_text.goto(0, 0)
            game_over_text.write("Game Over", align = "center", font = ("Georgia", 24, "normal"))
            time.sleep(2)
            game_over_text.clear()
            snake.goto(0, 0)
            snake.direction = "stop"
            score = 0
            score_display.clear()
            score_display.write("Score: 0", align = "center", font = ("Georgia", 24, "normal"))
    time.sleep(0.1)