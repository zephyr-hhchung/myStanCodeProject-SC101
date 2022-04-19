"""
File: my_drawing.py
Name: Hui-Hsuan Chung
-------------------------
Draw a view of Taipei 101 using the GObjects from campy
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow

# Open an empty window
window = GWindow(width=600, height=800)

def main():
    """
    Title: Taipei 101's view
    I went to Taipei 101 for the first time just a few days
    before I left for Germany to study abroad.
    I am happy that I've been here to enjoy the night at the tallest building in Taiwan.
    """
    # Background color
    make_rect(550, 750, 300, 400, 'lavender')
    make_rect(550, 100, 300, 600, 'lightskyblue')
    make_rect(550, 150, 300, 500, 'steelblue')

    # Transition background color
    make_rect(50, 10, 50, 650, 'lightskyblue')
    make_rect(50, 10, 150, 650, 'lightskyblue')
    make_rect(50, 10, 200, 650, 'lightskyblue')
    make_rect(50, 10, 280, 650, 'lightskyblue')
    make_rect(50, 10, 330, 650, 'lightskyblue')
    make_rect(50, 10, 380, 650, 'lightskyblue')
    make_rect(50, 10, 450, 650, 'lightskyblue')
    make_rect(50, 10, 530, 650, 'lightskyblue')
    make_rect(15, 7, 40, 657, 'lightskyblue')
    make_rect(25, 11, 70, 657, 'lightskyblue')
    make_rect(50, 8, 130, 657, 'lightskyblue')
    make_rect(40, 15, 210, 657, 'lightskyblue')
    make_rect(30, 10, 330, 657, 'lightskyblue')
    make_rect(50, 19, 390, 657, 'lightskyblue')
    make_rect(35, 5, 470, 657, 'lightskyblue')
    make_rect(15, 5, 530, 657, 'lightskyblue')
    make_rect(10, 10, 40, 580, 'steelblue')
    make_rect(50, 10, 100, 580, 'steelblue')
    make_rect(50, 10, 210, 580, 'steelblue')
    make_rect(50, 10, 270, 580, 'steelblue')
    make_rect(50, 10, 370, 580, 'steelblue')
    make_rect(50, 10, 400, 580, 'steelblue')
    make_rect(50, 10, 480, 580, 'steelblue')
    make_rect(20, 10, 520, 580, 'steelblue')
    make_rect(10, 10, 40, 585, 'lightskyblue')
    make_rect(50, 10, 70, 585, 'lightskyblue')
    make_rect(30, 10, 130, 585, 'lightskyblue')
    make_rect(40, 10, 210, 585, 'lightskyblue')
    make_rect(50, 10, 330, 585, 'lightskyblue')
    make_rect(10, 10, 390, 585, 'lightskyblue')
    make_rect(20, 10, 470, 585, 'lightskyblue')
    make_rect(20, 10, 530, 585, 'lightskyblue')

    # Background cloud
    make_circle(20, 500, 700, 'gainsboro')
    make_rect(115, 19, 440, 700, 'gainsboro')
    make_circle(20, 380, 700, 'gainsboro')
    make_circle(20, 450, 730, 'gainsboro')
    make_rect(88, 19, 400, 730, 'gainsboro')
    make_circle(20, 350, 730, 'gainsboro')

    # The moon
    make_circle(70, 450, 700, 'goldenrod')
    make_circle(68, 448, 700, 'gold')

    # Foreground cloud
    make_circle(20, 450, 650, 'snow')
    make_rect(45, 19, 425, 650, 'snow')
    make_circle(20, 400, 650, 'snow')
    make_circle(20, 430, 660, 'snow')
    make_rect(45, 19, 405, 660, 'snow')
    make_circle(20, 380, 660, 'snow')
    make_circle(20, 400, 665, 'snow')
    make_rect(45, 19, 375, 665, 'snow')
    make_circle(20, 350, 665, 'snow')
    make_circle(25, 480, 680, 'snow')
    make_rect(45, 23, 455, 680, 'snow')
    make_circle(25, 430, 680, 'snow')
    make_circle(25, 500, 690, 'snow')
    make_rect(45, 23, 475, 690, 'snow')
    make_circle(25, 450, 690, 'snow')

    # Mountain background
    make_rect(550, 150, 300, 400, 'cadetblue')

    # Transition background color
    make_rect(10, 10, 40, 470, 'steelblue')
    make_rect(50, 10, 100, 470, 'steelblue')
    make_rect(20, 10, 210, 470, 'steelblue')
    make_rect(50, 10, 270, 470, 'steelblue')
    make_rect(40, 10, 370, 470, 'steelblue')
    make_rect(30, 10, 400, 470, 'steelblue')
    make_rect(50, 10, 480, 470, 'steelblue')
    make_rect(20, 10, 520, 470, 'steelblue')
    make_rect(10, 5, 30, 469, 'steelblue')
    make_rect(40, 5, 90, 469, 'steelblue')
    make_rect(30, 5, 150, 469, 'steelblue')
    make_rect(40, 5, 230, 469, 'steelblue')
    make_rect(50, 5, 350, 469, 'steelblue')
    make_rect(20, 5, 400, 469, 'steelblue')
    make_rect(40, 5, 440, 469, 'steelblue')
    make_rect(10, 5, 550, 469, 'steelblue')

    # Mountains
    make_triangle(225, 550, 25, 200, 555, 200, 'teal')
    make_triangle(225, 550, 515, 200, 555, 200, 'darkcyan')
    make_triangle(125, 500, 25, 300, 325, 300, 'lightseagreen')
    make_triangle(125, 500, 305, 300, 325, 300, 'cadetblue')
    make_triangle(505, 450, 225, 300, 550, 350, 'darkcyan')
    make_triangle(505, 450, 225, 300, 300, 350, 'teal')

    # Background color
    make_rect(550, 300, 300, 175, 'midnightblue')

    # Building base color
    make_rect(20, 60, 130, 350, 'midnightblue')
    make_rect(30, 120, 60, 350, 'midnightblue')
    make_rect(30, 150, 160, 350, 'midnightblue')
    make_rect(40, 90, 180, 350, 'midnightblue')
    make_rect(20, 50, 200, 350, 'midnightblue')
    make_rect(30, 60, 300, 350, 'midnightblue')
    make_rect(20, 50, 420, 350, 'midnightblue')
    make_rect(30, 30, 550, 350, 'midnightblue')
    make_rect(30, 50, 50, 350, 'darkblue')
    make_rect(30, 70, 80, 350, 'darkblue')
    make_rect(30, 60, 100, 350, 'darkblue')
    make_rect(30, 90, 150, 350, 'darkblue')
    make_rect(30, 30, 250, 350, 'darkblue')
    make_rect(30, 40, 350, 350, 'darkblue')
    make_rect(30, 90, 380, 350, 'darkblue')
    make_rect(30, 120, 410, 380, 'darkblue')
    make_rect(30, 50, 450, 350, 'darkblue')
    make_rect(30, 50, 500, 350, 'darkblue')
    make_rect(550, 50, 300, 320, 'darkblue')

    # TPE 101
    make_ploy(280, 330, 280, 370, 320, 370, 320, 330, 'darkblue')
    make_ploy(280, 350, 275, 390, 325, 390, 320, 350, 'darkblue')
    make_ploy(280, 390, 275, 430, 325, 430, 320, 390, 'darkblue')
    make_ploy(280, 430, 275, 480, 325, 480, 320, 430, 'darkblue')
    make_ploy(280, 480, 275, 520, 325, 520, 320, 480, 'darkblue')
    make_ploy(280, 520, 275, 560, 325, 560, 320, 520, 'darkblue')
    make_rect(25, 40, 300, 570, 'darkblue')
    make_rect(9, 50, 300, 600, 'darkblue')

    # Building lights
    light_y = [360, 370, 380, 400, 410, 420, 450, 460, 470, 490, 500, 510, 530, 540, 550]
    for pos_y in light_y:
        make_rect(25, 2, 300, pos_y, 'yellow')
    make_rect(15, 1, 300, 575, 'yellow')
    make_rect(15, 1, 300, 580, 'yellow')

    # Small house 1
    make_rect(5, 5, 45, 360, 'gold')
    make_rect(5, 5, 55, 360, 'gold')
    make_rect(5, 5, 65, 360, 'gold')
    make_rect(5, 5, 75, 360, 'gold')
    make_rect(5, 5, 85, 360, 'gold')
    make_rect(5, 5, 95, 360, 'gold')
    make_rect(5, 5, 105, 360, 'gold')
    make_rect(70, 2, 75, 370, 'gold')

    # Small house 2
    make_rect(4, 4, 155, 360, 'gold')
    make_rect(4, 4, 145, 360, 'gold')
    make_rect(4, 4, 155, 370, 'gold')
    make_rect(4, 4, 145, 370, 'gold')
    make_rect(4, 4, 155, 380, 'gold')
    make_rect(4, 4, 145, 380, 'gold')

    # Small house 3
    make_rect(4, 3, 245, 350, 'gold')
    make_rect(4, 3, 245, 355, 'gold')
    make_rect(4, 3, 245, 360, 'gold')
    make_rect(4, 3, 255, 350, 'gold')
    make_rect(4, 3, 255, 355, 'gold')
    make_rect(4, 3, 255, 360, 'gold')

    # Small house 4
    make_rect(5, 2, 343, 350, 'gold')
    make_rect(5, 2, 343, 360, 'gold')
    make_rect(65, 2, 385, 350, 'gold')
    make_rect(65, 2, 385, 360, 'gold')
    make_rect(65, 2, 385, 350, 'gold')
    make_rect(65, 2, 385, 360, 'gold')
    make_rect(45, 2, 395, 375, 'gold')
    make_rect(45, 2, 395, 385, 'gold')
    make_rect(5, 5, 405, 408, 'gold')
    make_rect(5, 5, 405, 418, 'gold')
    make_rect(5, 5, 405, 428, 'gold')
    make_rect(5, 5, 415, 408, 'gold')
    make_rect(5, 5, 415, 418, 'gold')
    make_rect(5, 5, 415, 428, 'gold')

    # Small house 5
    make_rect(4, 4, 445, 355, 'gold')
    make_rect(4, 4, 445, 365, 'gold')
    make_rect(4, 4, 455, 355, 'gold')
    make_rect(4, 4, 455, 365, 'gold')

    # Small house 5
    make_rect(4, 4, 505, 355, 'gold')
    make_rect(4, 4, 505, 365, 'gold')
    make_rect(4, 4, 495, 355, 'gold')
    make_rect(4, 4, 495, 365, 'gold')

    # Transition building color
    make_rect(10, 15, 30, 290, 'darkblue')
    make_rect(40, 15, 90, 290, 'darkblue')
    make_rect(30, 15, 150, 290, 'darkblue')
    make_rect(40, 15, 230, 290, 'darkblue')
    make_rect(50, 15, 290, 290, 'darkblue')
    make_rect(50, 15, 350, 290, 'darkblue')
    make_rect(20, 15, 400, 290, 'darkblue')
    make_rect(40, 15, 440, 290, 'darkblue')
    make_rect(40, 15, 490, 290, 'darkblue')
    make_rect(10, 15, 550, 290, 'darkblue')
    make_rect(10, 15, 35, 280, 'darkblue')
    make_rect(40, 15, 85, 280, 'darkblue')
    make_rect(30, 15, 130, 280, 'darkblue')
    make_rect(40, 15, 190, 280, 'darkblue')
    make_rect(50, 15, 250, 280, 'darkblue')
    make_rect(50, 15, 380, 280, 'darkblue')
    make_rect(20, 15, 410, 280, 'darkblue')
    make_rect(40, 15, 450, 280, 'darkblue')
    make_rect(40, 15, 500, 280, 'darkblue')
    make_rect(10, 15, 520, 280, 'darkblue')
    make_rect(10, 15, 55, 270, 'darkblue')
    make_rect(40, 15, 115, 270, 'darkblue')
    make_rect(30, 15, 180, 270, 'darkblue')
    make_rect(40, 15, 220, 270, 'darkblue')
    make_rect(40, 15, 350, 270, 'darkblue')
    make_rect(40, 15, 420, 270, 'darkblue')
    make_rect(10, 15, 550, 270, 'darkblue')
    make_rect(10, 15, 85, 260, 'darkblue')
    make_rect(40, 15, 150, 260, 'darkblue')
    make_rect(30, 15, 240, 260, 'darkblue')
    make_rect(40, 15, 350, 260, 'darkblue')
    make_rect(40, 15, 450, 260, 'darkblue')
    make_rect(40, 15, 550, 260, 'darkblue')
    make_rect(10, 15, 570, 260, 'darkblue')
    make_rect(40, 15, 150, 250, 'darkblue')
    make_rect(30, 15, 310, 250, 'darkblue')
    make_rect(20, 15, 350, 250, 'darkblue')
    make_rect(30, 15, 360, 250, 'darkblue')
    make_rect(20, 15, 420, 250, 'darkblue')
    make_rect(30, 15, 500, 250, 'darkblue')
    make_rect(10, 15, 520, 250, 'darkblue')


# Create several functions in the following to add a given object to the window
def make_circle(size, pos_x, pos_y, color):
    circle = GOval(size, size, x=pos_x - size / 2., y=window.height - pos_y - size / 2)
    circle.filled = True
    circle.fill_color = color
    circle.color = color
    return window.add(circle)


def make_oval(size1, size2, pos_x, pos_y, color):
    oval = GOval(size1, size2, x=pos_x - size1 / 2., y=window.height - pos_y - size2 / 2.)
    oval.filled = True
    oval.fill_color = color
    oval.color = color
    return window.add(oval)


def make_square(size, pos_x, pos_y, color):
    square = GRect(size, size, x=pos_x - size / 2., y=window.height - pos_y - size / 2.)
    square.filled = True
    square.fill_color = color
    square.color = color
    return window.add(square)


def make_rect(size1, size2, pos_x, pos_y, color):
    rect = GRect(size1, size2, x=pos_x - size1 / 2., y=window.height - pos_y - size2 / 2.)
    rect.filled = True
    rect.fill_color = color
    rect.color = color
    return window.add(rect)


def make_triangle(x1, y1, x2, y2, x3, y3, color):
    triangle = GPolygon()
    triangle.add_vertex((x1, window.height - y1))
    triangle.add_vertex((x2, window.height - y2))
    triangle.add_vertex((x3, window.height - y3))
    triangle.filled = True
    triangle.fill_color = color
    triangle.color = color
    return window.add(triangle)


def make_ploy(x1, y1, x2, y2, x3, y3, x4, y4, color):
    poly1 = GPolygon()
    poly1.add_vertex((x1, window.height - y1))
    poly1.add_vertex((x2, window.height - y2))
    poly1.add_vertex((x3, window.height - y3))
    poly1.add_vertex((x4, window.height - y4))
    poly1.filled = True
    poly1.fill_color = color
    poly1.color = color
    return window.add(poly1)


if __name__ == '__main__':
    main()
