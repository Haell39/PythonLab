import collections
import random
import time
import turtle

spawn_interval = 0.1
ball_speed = 4
increase_rotation_step = 0.25
colour_change_interval = 4
frame_rate = 20
time_per_frame = 1 / frame_rate

# Set up window
window =  turtle.Screen()
window.bgcolor(0.2, 0.2, 0.2)
window.tracer(0)
window.bounce_on = True
window.title("Bouncing off edges: ON")

spinner = turtle.Turtle()
spinner.color("white")
spinner.rotation_speed = 2

# Spawn new balls
colour = random.random(), random.random(), random.random()

balls = []
pool_of_balls = []

def spawn_ball(reference):
    if pool_of_balls:
        balls.append(pool_of_balls.pop())
        balls[-1].showturtle()
    else:
        balls.append(turtle.Turtle())
    balls[-1].shape("circle")
    balls[-1].color(colour)
    balls[-1].turtlesize(0.5)
    balls[-1].penup()
    balls[-1].setposition(reference.position())
    balls[-1].setheading(reference.heading())

# Change speed of rotation
def increase_anticlockwise_rotation():
    spinner.rotation_speed += increase_rotation_step

def decrease_anticlockwise_rotation():
    spinner.rotation_speed -= increase_rotation_step

def toggle_bouncing():
    window.bounce_on = not window.bounce_on
    window.title(
        f"Bouncing off edges: {'ON' if window.bounce_on else 'OFF'}"
    )

window.onkeypress(increase_anticlockwise_rotation, "Left")
window.onkeypress(decrease_anticlockwise_rotation, "Right")
window.onkeypress(toggle_bouncing, "space")
window.listen()

# Main animation loop
spawn_timer = time.time()
ball_colour_timer = time.time()
last_100_frames = collections.deque(maxlen=100)
while True:
    frame_start_time = time.time()
    spinner.left(spinner.rotation_speed)

    # Spawn new ball
    if time.time() - spawn_timer > spawn_interval:
        spawn_ball(spinner)
        spawn_timer = time.time()

    # Change ball colour
    if time.time() - ball_colour_timer > colour_change_interval:
        colour = random.random(), random.random(), random.random()
        ball_colour_timer = time.time()

    # Move all balls and clear balls that leave the screen
    for ball in balls.copy():
        ball.forward(ball_speed)

        # Check if ball has hit a screen edge
        if window.bounce_on:
            # Check if ball has hit left or right wall
            if abs(ball.xcor()) > window.window_width() / 2:
                angle = 180 - ball.heading()
                ball.setheading(angle)

            # Check if ball has hit top or bottom wall
            elif abs(ball.ycor()) > window.window_height() / 2:
                angle = 360 - ball.heading()
                ball.setheading(angle)
        else:  # bouncing is turned off
            if (
                    abs(ball.xcor()) > window.window_width() / 2
                    or abs(ball.ycor()) > window.window_height() / 2
            ):
                ball.hideturtle()
                balls.remove(ball)
                pool_of_balls.append(ball)

    window.update()
    frame_time = time.time() - frame_start_time
    if frame_time < time_per_frame:
        time.sleep(time_per_frame - frame_time)
    last_100_frames.append(time.time() - frame_start_time)
    print(sum(last_100_frames) / len(last_100_frames))