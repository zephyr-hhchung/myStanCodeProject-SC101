"""
File: bouncing_ball.py
Name: Hui-Hsuan Chung
-------------------------
The program is to stimulate a bouncing ball for 3 times.
The ball will only start to fall when it is at its starting position (START_X, START_Y).
The ball's trajectory is based on the given velocity, gravity, and a reduced velocity factor when hitting the ground.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants given in the assignment
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Initial y velocity
VY = 0

# Maximal 3 trials for the ball to fall
TRIAL = 3

# The switch to decide whether the ball will fall (0:close, 1:open)
SWITCH = 1

# Open a window
window = GWindow(800, 500, title='bouncing_ball.py')

# Create a ball on the window for a given size and a position
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.fill_color = True
ball.filled = 'black'
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Activate the mouse click mode.
    # When a click is detected and the switch is open, the ball will fall.
    onmouseclicked(click_ball)


def click_ball(mouse):
    global SWITCH, TRIAL, ball
    # Run the program when the switch is open (switch=1) and there is still free trials (trial>0)
    if SWITCH == 1 and TRIAL > 0:
        # When the program start, close the switch and deduct one trial
        SWITCH = 0
        TRIAL -= 1
        # Set the starting position and velocity for x and y axis
        pos_x = START_X
        pos_y = START_Y
        vel_x = VX
        vel_y = VY
        # Make the ball falling: before the ball leaves the window, the ball continues to move
        while pos_x < window.width:
            # Remove the ball from it's old position
            window.remove(ball)
            # Update the x/y position and the y velocity that is accelerated by the gravity
            pos_x = pos_x + vel_x*1.
            vel_y = vel_y + GRAVITY*1.
            pos_y = pos_y + vel_y*1.
            # When the ball hits the ground, the ball bounces back with a reduced velocity by 10%
            if pos_y > window.height-SIZE and vel_y > 0.:
                vel_y = -1. * vel_y * REDUCE
            # Add the ball's updated position
            ball = GOval(SIZE, SIZE, x=pos_x, y=pos_y)
            ball.fill_color = True
            ball.filled = 'black'
            window.add(ball)
            pause(DELAY)
        # When the ball moves out of the window, make a new ball at the initial starting position
        if pos_x > window.width:
            ball.x = START_X
            ball.y = START_Y
            window.add(ball)
        # Open the switch again
        SWITCH = 1


if __name__ == "__main__":
    main()
