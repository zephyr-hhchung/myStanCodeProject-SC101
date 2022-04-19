"""
File: babygraphics.py
Name: Hui-Hsuan Chung
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
SCALE_Y = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000  # Factor to scale the rank to make it fit the y axis


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # Calculate the step size based on the given years, canvas window size, and its margin size
    size_step = int((width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    # Return the x position: the margin size + step size * year index
    return GRAPH_MARGIN_SIZE + year_index * size_step


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas
    # ----- Write your code below this line ----- #
    # Plot the upper horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # Plot the lower horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    # Plot the vertical lines with a given width
    for i_year in range(len(YEARS)):
        x_pos_line = get_x_coordinate(CANVAS_WIDTH, i_year)                          # Get the line's x-axis position
        canvas.create_line(x_pos_line, 0, x_pos_line, CANVAS_HEIGHT)                 # Plot the line
        canvas.create_text(x_pos_line + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,  # Add the year info in the x-axis
                           text=YEARS[i_year], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    # ----- Write your code below this line ----- #
    x_pos_line, y_pos_line = 0, 0     # Variables used to store the previous x/y-position when plotting a line
    for i_name, lookup_name in enumerate(lookup_names):  # Inspect the names
        color = COLORS[int(i_name % len(COLORS))]        # Assign a given color for a given name
        for i_year, year in enumerate(YEARS):            # Inspect the years
            x_pos_data = get_x_coordinate(CANVAS_WIDTH, i_year)  # Get x position at a given year
            x_pos_text = x_pos_data + TEXT_DX                    # The name text's x position

            # If the name HAS a rank in the given year
            if str(year) in name_data[lookup_name]:
                y_pos_data = GRAPH_MARGIN_SIZE + int(name_data[lookup_name][str(year)]) * SCALE_Y  # data's y position
                mark_name = lookup_name + ' ' + name_data[lookup_name][str(year)]  # Set the name marker
                canvas.create_text(x_pos_text, y_pos_data, text=mark_name, anchor=tkinter.SW, fill=color)  # Add mark
                if i_year > 0:  # Plot a line (starting from the 2nd data point)
                    canvas.create_line(x_pos_line, y_pos_line, x_pos_data, y_pos_data, width=LINE_WIDTH, fill=color)
                x_pos_line = x_pos_data  # Update the variables for plotting lines
                y_pos_line = y_pos_data  # Update the variables for plotting lines

            # If the name DOES NOT have a rank in the given year
            else:
                y_pos_data = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE   # Set the y position to the bottom
                mark_name = lookup_name + ' *'                   # Set the name marker to '{name} *'
                canvas.create_text(x_pos_text, y_pos_data, text=mark_name, anchor=tkinter.SW, fill=color)
                if i_year > 0:  # Plot a line (starting from the 2nd data point)
                    canvas.create_line(x_pos_line, y_pos_line, x_pos_data, y_pos_data, width=LINE_WIDTH, fill=color)
                x_pos_line = x_pos_data  # Update the variables for plotting lines
                y_pos_line = y_pos_data  # Update the variables for plotting lines


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
