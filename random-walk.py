import turtle as t
import random

# Create turtle object
tim = t.Turtle()

# Enable RGB color mode (0–255)
t.colormode(255)


def random_color():
    """Generate and return a random RGB color tuple.

    Returns:
        tuple: (r, g, b) where each value is between 0 and 255.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Set pen thickness and drawing speed
tim.pensize(15)
tim.speed("fastest")

# List of possible directions (in degrees)
directions = [0, 90, 180, 270]

# Draw 300 random steps with random colors and directions
for _ in range(300):
    tim.pencolor(random_color())          # Set random pen color
    tim.setheading(random.choice(directions))  # Choose random direction
    tim.forward(30)                       # Move forward