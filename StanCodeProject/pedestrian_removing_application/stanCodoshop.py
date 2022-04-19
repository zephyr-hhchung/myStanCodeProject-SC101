"""
File: stanCodoshop.py
Name: Hui-Hsuan Chung
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # Calculate the color distance
    color_dist = ((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)**0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    r, g, b = 0, 0, 0       # Variables to store the cumulative pixel values
    n_pix = len(pixels)     # Numbers of the input pixel list
    # Add the pixel values together and average them
    for pixel in pixels:
        r += pixel.red
        g += pixel.green
        b += pixel.blue
    ave_r = int(r/n_pix)
    ave_g = int(g/n_pix)
    ave_b = int(b/n_pix)
    return [ave_r, ave_g, ave_b]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    ave_r, ave_g, ave_b = get_average(pixels)    # Get the average pixel values
    pix_lst = []                                 # A list to store the Pixel and its color distance to the average Pixel
    for pixel in pixels:                         # Scan the input pixels
        get_pixel_dist(pixel, ave_r, ave_g, ave_b)
        pix_lst.append((get_pixel_dist(pixel, ave_r, ave_g, ave_b), pixel))
    best_pix = sorted(pix_lst, key=lambda ele: ele[0])[0][1]   # Sort the list based on color distance only
    return best_pix


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):                                  # Scan the pixels along the width
        for y in range(height):                             # Scan the pixels along the height
            pix_list = []                                   # A list to store the Pixel objects at (x, y)
            for image in images:                            # Scan the input images
                pix_list.append(image.get_pixel(x, y))
            best = get_best_pixel(pix_list)                 # Get the best pixel (with the shortest color distance)
            result.set_pixel(x, y, best)                    # Add the best pixel to the result image
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
