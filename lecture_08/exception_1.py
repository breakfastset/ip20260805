print("-- A Simple Division Calculator --")

try:
    num_1 = int(input("Enter an integer: "))
    divisor = int(input("Enter an integer divisor: "))

    result = num_1 // divisor
    remainder = num_1 % divisor
    print("Result is ", result)
    print("Remainder is ", remainder)
except ValueError:
    print("Please enter INTEGERS ONLY!")
except ZeroDivisionError:
    print("Divisor cannot be 0!")
except:   # Catch everything else
    print("Something went wrong! But I don't know why!")
else:   # only run if there are no exceptions
    print("All inputs are correct!")
finally:  # run in all circumstances
    print("Will always run regardless of error!")

print("-- Thank you for using our App --")