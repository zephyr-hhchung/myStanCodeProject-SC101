"""
File: draw_line.py
Name: Hui-Hsuan Chung
-------------------------
The code is used for creating lines.
The user first clicks at the starting point and second click will link the two points into a line.
The code will identify the odd clicks and create circles on the clicks.
Then, the code will identify the even to make lines based on the previous click.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 10
COUNT = 0

# Variables to store the positions from the even clicks
x_even = 0
y_even = 0

# Create a window
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # Activate the mouse event mode, in each click, the code will call the draw function
    onmouseclicked(draw)


def draw(mouse):
    global COUNT, x_even, y_even
    # Save how many times the user has clicked in COUNT
    COUNT += 1
    # Create a circle with a given size
    pen_stroke = GOval(SIZE, SIZE)
    # For odd clicks
    if COUNT % 2 != 0:
        x_even = mouse.x
        y_even = mouse.y
        # Add the circle to the window based on the clicked positions
        window.add(pen_stroke, x=x_even-SIZE/2, y=y_even-SIZE/2)
    # For even clicks
    else:
        x_odd = mouse.x
        y_odd = mouse.y
        # Delete the circle
        circle_even = window.get_object_at(x_even, y_even)
        window.remove(circle_even)
        # Create a line based on the clicked positions
        line = GLine(x_even, y_even, x_odd, y_odd)
        window.add(line)


if __name__ == "__main__":
    main()
