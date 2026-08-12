import turtle as t
import random

# Create turtle and screen objects
tim = t.Turtle()
s = t.Screen()

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


# Set maximum drawing speed
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    """Draw a spirograph pattern by rotating circles.

    Args:
        size_of_gap (int): Angle gap (in degrees) between each circle.
    """
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# Draw spirograph with 3-degree gap
draw_spirograph(size_of_gap=3)

# Keep window open until click
s.exitonclick()