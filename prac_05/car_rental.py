MENU="""
---------------------------------------
|    Welcome to Minimal Car Rental    |
---------------------------------------
0. Check Car Availability
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
    car_count = int(input("Number of cars to rent? "))
    if car_count > 0:
        if num_cars >= car_count:
            num_cars -= car_count
            print(f"Your requested {car_count} cars is/are available at check out")
        else:
            print("Sorry, there are no available cars at the moment.")
    else:
        print("Invalid number of cars. Must be > 0 !!!")
    return num_cars


def return_car(num_cars):
    """Increase the number of available cars based on user's input."""
    car_count = int(input("Number of cars to return? "))
    if car_count > 0:
        num_cars += car_count
        print(f"{car_count} car(s) returned. Thank you!")
    else:
        print("Invalid number of cars. Must be > 0 !!!")
    return num_cars


def display_availability(availability):
    """Display the number of available cars."""
    print(f"Available cars: {availability}")


def main():
    """Start program."""
    availability = read_availability(CARS_DB_FILE)
    # print("Available cars:", availability)  # for DEBUGGING purpose
    choice = input(MENU)   # 1. and 2. print and ask user for choice

    # 3. display choice and update availability if necessary
    if choice == "0":
        print_pretty_title("0. Check Car Availability")
        display_availability(availability)      # a)
    elif choice == "1":
        print_pretty_title("1. Rent Car")
        availability = rent_car(availability)   # get the updated availability
    elif choice == "2":
        print_pretty_title("2. Return Car")
        availability = return_car(availability)
    elif choice == "3":
        print_pretty_title("3. Read Terms and Conditions")
    elif choice == "4":
        print("4. Quit")
    else:
        print("Options 1 to 4 only!")    # c)

    write_availability(CARS_DB_FILE, availability)   # update to the file.    `
    print("-=-= Thank you for using Minimal Car Rental =-=-")

main()