from maths_functions import *     # our custom module 'maths_functions'

# def <function_name> (<parameter(s)>):
#      ...
#      ...
#      return .... (optional)

def print_title(title_text):                  # title_text is a parameter
    """Print a title in a banner."""
    print("-" * 40)
    print(f"| {title_text:^36} |")
    print("-" * 40)   # does not return any value (void function)

def main():
    print_title(" Maths Functions ")          # " Maths Functions " is the argument
    print(f"Area of circle (r=10): {circle_area(10)}")
    print(f"Area of circle (r=7): {circle_area(7)}")
    print(f"Volume of sphere (r=10): {sphere_volume(10)}")
    print(f"Surface area of sphere (r=10): {sphere_surface_area(10)}")
    print()
    x = 1
    y = 2
    z = 3
    new_x, new_y, new_z = translate_3d_point(x, y, z, 10)
    print(f"After translation: ({new_x}, {new_y}, {new_z})")
    # print(my_x)   # local variable in translate_3d_point() => ERROR!

    print("-------------------- End  --------------------- ")

main()   # call the main function