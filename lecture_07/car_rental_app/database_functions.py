def read_availability(filename):
    """Read car availability from a file."""
    cars = []
    in_file = open(filename, "r")
    for line in in_file:
        new_car = line.split(",")   # each line is a new car type
        new_car[-1] = int(new_car[-1])   # convert last column to int
        cars.append(new_car)
    in_file.close()
    return cars

# TODO: Update write_availability to write to csv
def write_availability(filename, num_cars):
    """Write the updated number of cars to a file."""
    out_file = open(filename, "w")
    line = f"{num_cars}\n"     # Convert num_cars to str before writing
    out_file.write(line)
    out_file.close()


if __name__ == '__main__':
    car_list = read_availability("cars.csv")
    print(car_list)