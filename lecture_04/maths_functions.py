import math

def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2    # value returning function

def sphere_volume(radius):
    """Return the volume of a sphere."""
    return 4 / 3 * math.pi * radius ** 3

def sphere_surface_area(radius):
    """Return surface area of a sphere."""
    return 4 * math.pi * radius ** 2

def translate_3d_point(x, y, z, distance):
    """Translate a 3d point by given distance."""
    my_x = x + distance                 # my_x is a local variable
    my_y = y + distance                 # and therefore temporary in this function
    my_z = z + distance
    return my_x, my_y, my_z             # these variables will exist until this line
