MENU="""
---------------------------------------
|    Welcome to Minimal Car Rental    |
---------------------------------------
1. Rent Car
2. Return Car
3. Read Terms and Conditions
4. Quit
>> """

CARS_DB_FILE = "cars.txt"

def print_pretty_title(title_name):
    """Print title in a pretty way."""
    length = len(title_name)
    print("=" * (length + 10))
    print(f"|    {title_name}    |")
    print("=" * (length + 10))


def read_availability(filename):
    """Read car availability from a file."""
    in_file = open(filename, "r")
    num_cars = int(in_file.readline())
    in_file.close()
    return num_cars


def write_availability(filename, num_cars):
    """Write the updated number of cars to a file."""
    out_file = open(filename, "w")
    line = f"{num_cars}\n"     # Convert num_cars to str before writing
    out_file.write(line)
    out_file.close()


def rent_car(num_cars):
    """Rent a car if available and update the availability."""
    if num_cars > 0:
        num_cars -= 1
        print("Your car is available at check out")
    else:
        print("Sorry, there are no available cars at the moment.")
    return num_cars


def return_car(num_cars):
    """Increase the number of available cars."""
    num_cars += 1
    print("Car returned. Thank you!")
    return num_cars


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
    availability = read_availability(CARS_DB_FILE)
    print("Available cars:", availability) # debugging

    # B. Menu options
    choice = input(MENU)   # 1. init choice to go into the loop

    while choice != "4":   # 2. while condition is True
        if choice == "1":    # 3. Body of statements
            print_pretty_title("1. Rent Car")
            availability = rent_car(availability)   # get the updated availability
        elif choice == "2":
            print_pretty_title("2. Return Car")
            availability = return_car(availability)
        elif choice == "3":
            print_pretty_title("3. Read Terms and Conditions")
            display_terms_conditions("terms_conditions.txt")
        else:
            print("Options 1 to 4 only!")

        choice = input(MENU)    # 4. alter var to exit condition in 2.

    write_availability(CARS_DB_FILE, availability)   # update to the file.    `
    print("-=-= Thank you for using Minimal Car Rental =-=-")

main()