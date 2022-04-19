"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
------------------------------
The class object - BreakoutGraphics is used for breakout game
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    """
    The Class for setting up the Breakout games
    """
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_width = window_width
        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.window_height = window_height

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width-paddle_width)/2., y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.move(dx=0, dy=0)
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2, x=(self.window_width-self.ball_radius)/2.,
                          y=(self.window_height-self.ball_radius)/2.)
        # Reset the ball position
        self.reset_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.pad_move)
        self.is_moving = False
        onmouseclicked(self.mouse_click)

        # Draw bricks
        self.brick_pos_x = 0
        self.brick_pos_y = BRICK_OFFSET
        colors = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue']  # Brick color
        for cols in range(brick_cols):
            for i, rows in enumerate(range(brick_rows)):
                self.brick_pos_y += (BRICK_SPACING+BRICK_HEIGHT)
                c_index = i % 10
                self.make_brick(colors[c_index])
            self.brick_pos_x += (BRICK_SPACING+BRICK_WIDTH)
            self.brick_pos_y = BRICK_OFFSET

        self.win_label = GLabel("You Win!", x=self.window_width/2., y=self.window_height/2.)     # Label for winners
        self.lose_label = GLabel("Game Over!", x=self.window_width/2., y=self.window_height/2.)  # Label for losers

    def make_brick(self, color):
        """
        Create a brick with a specified color
        """
        brick = GRect(self.brick_width, self.brick_height, x=self.brick_pos_x, y=self.brick_pos_y)
        brick.filled = True
        brick.color = color
        brick.fill_color = color
        self.window.add(brick)

    def pad_move(self, event):
        """
        Move the paddle based on the event position
        """
        if event.x > self.window_width - self.paddle_width/2.:
            self.paddle.x = self.window_width - self.paddle_width
        elif event.x < self.paddle_width/2.:
            self.paddle.x = 0.
        else:
            self.paddle.x = event.x - self.paddle_width/2
        self.paddle.y = self.window_height-self.paddle_offset
        self.window.add(self.paddle)

    def mouse_click(self, event):
        """
        Initialize the moving state of the ball
        """
        self.is_moving = True

    def set_ball_velocity(self):
        """
        Reset the ball velocity randomly
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        """
        Reset the ball position to the starting position
        """
        self.ball.x = (self.window_width-self.ball_radius)/2.
        self.ball.y = (self.window_height-self.ball_radius)/2.
        self.ball.filled = True
        self.window.add(self.ball)

    def get_ball_vx(self):
        """
        Return the private instance variable, the x-axis velocity of the ball
        """
        return self.__dx

    def get_ball_vy(self):
        """
        Return the private instance variable, the y-axis velocity of the ball
        """
        return self.__dy

    def win(self):
        """
        Show the GLabel object for winners on the GWindow
        """
        self.window.add(self.win_label)

    def lose(self):
        """
        Show the GLabel object for losers on the GWindow
        """
        self.window.add(self.lose_label)
