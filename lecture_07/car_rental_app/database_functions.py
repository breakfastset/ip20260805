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


def write_availability(filename, car_list):
    """Write the updated number of cars to a file."""
    out_file = open(filename, "w")
    for car in car_list:
        car[-1] = str(car[-1])    # convert int to str
        line = ",".join(car)  # join all items in list with , as delimiter
        out_file.write(line + "\n")

    out_file.close()


def main():
    print("Test 1: Read Availability")
    car_list = read_availability("cars.csv")
    print(car_list)
    car_list[0][-1] += 2
    print(car_list)
    print()

    print("Test 2: Write Availability")
    write_availability("cars.csv", car_list)

if __name__ == '__main__':  # run main() if you are running this file.
    main()