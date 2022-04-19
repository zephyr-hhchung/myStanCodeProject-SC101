"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
------------------------------
The program starts the breakout game
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constants
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This program runs a game 'Breakout'
    A ball will be bouncing around the GWindow
    The players need to move the paddle to bounce the ball to touch all the bricks
    The game will start by a clicks when there is available lives to play
    """
    live = NUM_LIVES                        # Counts how many times the ball can go out of the window
    graphics = BreakoutGraphics()           # Initialize the game setting
    r_ball = graphics.ball_radius           # The radius of the ball
    graphics.set_ball_velocity()            # Initialize the ball velocity
    vel_x = graphics.get_ball_vx()
    vel_y = graphics.get_ball_vy()
    num_brick = graphics.brick_rows * graphics.brick_cols  # The numbers of the bricks

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        # When the ball is moving and we have enough lives to play the game
        if graphics.is_moving and live > 0:
            graphics.ball.move(dx=vel_x, dy=vel_y)  # Make the ball move
            pos_x = graphics.ball.x
            pos_y = graphics.ball.y
            # Wall boundary bouncing settings
            if pos_x + 2*r_ball > graphics.window_width or pos_x < 0:   # The ball hits left and right walls
                vel_x *= -1                                             # x-axis velocity changes
            if pos_y < 0:                                               # The ball hit the upper walls
                vel_y *= -1                                             # y-axis velocity changes
            if pos_y > graphics.window_height:                          # The ball fall out of the window.
                live -= 1                                               # we lost 1 life
                graphics.is_moving = False                              # Stop the ball and reset position and velocity
                graphics.reset_ball()                                   # reset ball position
                graphics.set_ball_velocity()                            # reset ball velocity
                vel_x = graphics.get_ball_vx()
                vel_y = graphics.get_ball_vy()
                if live == 0:                                           # When losing the game, we run out of lives
                    graphics.lose()                                     # Game Over!
                    break
            # Check for collisions at the four corners of the ball
            # Check the 1st corner
            if graphics.window.get_object_at(pos_x, pos_y) is not None:
                # Hit a brick: remove the brick and bounce back
                if graphics.window.get_object_at(pos_x, pos_y) != graphics.paddle:
                    graphics.window.remove(graphics.window.get_object_at(pos_x, pos_y))
                    num_brick -= 1
                    vel_y *= -1
                # Hit the paddle: bounce back
                elif graphics.window.get_object_at(pos_x, pos_y) == graphics.paddle and vel_y > 0.:
                    vel_y *= -1
            # Check the 2nd corner
            elif graphics.window.get_object_at(pos_x, pos_y+2*r_ball) is not None:
                vel_y *= -1
                # Hit a brick: remove the brick and bounce back
                if graphics.window.get_object_at(pos_x, pos_y+2*r_ball) != graphics.paddle:
                    graphics.window.remove(graphics.window.get_object_at(pos_x, pos_y+2*r_ball))
                    num_brick -= 1
                    # Hit the paddle: bounce back
                elif graphics.window.get_object_at(pos_x, pos_y+2*r_ball) == graphics.paddle and vel_y > 0.:
                    vel_y *= -1
            # Check the 3rd corner
            elif graphics.window.get_object_at(pos_x+2*r_ball, pos_y) is not None:
                vel_y *= -1
                # Hit a brick: remove the brick and bounce back
                if graphics.window.get_object_at(pos_x+2*r_ball, pos_y) != graphics.paddle:
                    graphics.window.remove(graphics.window.get_object_at(pos_x+2*r_ball, pos_y))
                    num_brick -= 1
                    # Hit the paddle: bounce back
                elif graphics.window.get_object_at(pos_x+2*r_ball, pos_y) == graphics.paddle and vel_y > 0.:
                    vel_y *= -1
            # Check the 4th corner
            elif graphics.window.get_object_at(pos_x+2*r_ball, pos_y+2*r_ball) is not None:
                vel_y *= -1
                # Hit a brick: remove the brick and bounce back
                if graphics.window.get_object_at(pos_x+2*r_ball, pos_y+2*r_ball) != graphics.paddle:
                    graphics.window.remove(graphics.window.get_object_at(pos_x+2*r_ball, pos_y+2*r_ball))
                    num_brick -= 1
                    # Hit the paddle: bounce back
                elif graphics.window.get_object_at(pos_x+2*r_ball, pos_y+2*r_ball) == graphics.paddle and vel_y > 0.:
                    vel_y *= -1
            else:                   # No collisions
                pass                # The ball continues to move

            if num_brick == 0:      # When winning the game, we have zero brick left
                graphics.win()      # You win the game!
                break


if __name__ == '__main__':
    main()
