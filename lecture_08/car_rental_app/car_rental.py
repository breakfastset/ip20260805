from database_functions import *

MENU="""
---------------------------------------
|    Welcome to Minimal Car Rental    |
---------------------------------------
1. Rent Car
2. Return Car
3. Read Terms and Conditions
4. Quit
>> """

CARS_DB_FILE = "cars.csv"

def print_pretty_title(title_name):
    """Print title in a pretty way."""
    length = len(title_name)
    print("=" * (length + 10))
    print(f"|    {title_name}    |")
    print("=" * (length + 10))


def display_cars(car_list):
    """Display cars in an indexed manner."""
    print(" No        Make          Model      Class   Qty ")
    print("---- ---------------- ------------ ------- -----")
    for i in range(len(car_list)):
        make = car_list[i][0]
        model = car_list[i][1]
        car_class = car_list[i][2]
        quantity = car_list[i][3]
        print(f"{i:3}) {make:16} {model:12} {car_class:7} {quantity:5}")


def get_car_choice(car_list):
    """Get a valid car choice."""
    valid_choice = False        # assume that choice is invalid
    while not valid_choice:     # while choice is invalid
        try:
            choice = int(input("Choice? "))
            while choice < 0 or choice >= len(car_list):
                print(f"Choice must be between 0 and {len(car_list)-1}")
                choice = int(input("Choice? "))
            valid_choice = True    # if no errors, this is a valid choice
        except ValueError:
            print(f"Choice must be between 0 and {len(car_list)-1}")
    return choice


def rent_car(car_list):
    """Display list of available cars to choose from and update the car list."""
    # 1. Display the list of cars to choose
    display_cars(car_list)

    # 2. Get user input on the car chosen
    choice = get_car_choice(car_list)

    # 3. Update the quantity of the list within car_list
    selected_car = car_list[choice]
    quantity = car_list[choice][-1]
    if quantity > 0:
        car_list[choice][-1] -= 1
        print(f"Your {selected_car[0]} {selected_car[1]} is available at check out.")
    else:
        print(f"No availability for {selected_car[0]} {selected_car[1]}.")

    # 4. return car_list
    return car_list


def return_car(car_list):
    """Increase the number of available cars."""
    # 1. Display the cars
    display_cars(car_list)

    # 2. Get from list of cars to return
    choice = get_car_choice(car_list)

    # 3. update the number of cars for the returned make and model
    selected_car = car_list[choice]
    selected_car[-1] += 1
    print(f"{selected_car[0]} {selected_car[1]} returned. Thank you!")

    # 4. return car list
    return car_list


def display_terms_conditions(filename):
    """Read terms from file and display nicely to user."""
    line_count = 1
    in_file = open(filename, "r")
    for line in in_file.readlines():
        print(line)
        if line_count % 10 == 0:
            dummy = input("[[   Press Enter to continue...   ]]")
        line_count += 1
    in_file.close()


def main():
    """Start program."""
    # A. Load file into program
    car_list = read_availability(CARS_DB_FILE)
    # print("Available cars:", car_list) # debugging

    # B. Menu options
    choice = input(MENU)   # 1. init choice to go into the loop

    while choice != "4":   # 2. while condition is True
        if choice == "1":    # 3. Body of statements
            print_pretty_title("1. Rent Car")
            car_list = rent_car(car_list)   # get the updated availability
        elif choice == "2":
            print_pretty_title("2. Return Car")
            car_list = return_car(car_list)
        elif choice == "3":
            print_pretty_title("3. Read Terms and Conditions")
            display_terms_conditions("terms_conditions.txt")
        else:
            print("Options 1 to 4 only!")

        choice = input(MENU)    # 4. alter var to exit condition in 2.

    write_availability(CARS_DB_FILE, car_list)   # update to the file.    `
    print("-=-= Thank you for using Minimal Car Rental =-=-")

main()