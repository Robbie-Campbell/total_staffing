
# Reads in how many full time staff members are to be calculated
y = int(input("How many full time employees do you need to work out: "))

# Create a function which passes in the user input
def full_time(y):

    # Create 2 base variables
    i = 0
    total_hours = 0

    # Loops until the number of staff members have been represented
    while i < y:
        i += 1
        x = input("What is their hourly rate?: ")
        x = float(x) * (8 * 5 * 48)
        total_hours += x

    # Record the total money value of all full time staff
    full_time_hours = total_hours
    temps = input("Do you need to work out temp staff too? (y/n): ")

    # Run a function to work out the part time staff with a slightly different algorithm to work out total money value
    if temps == "y":
        how_many = int(input("How many temps do you need to work out?: "))
        i = 0
        total_hours = 0
        while i < how_many:
            i += 1
            x = input("What is their hourly rate?: ")
            x = float(x) * (8 * 3 * 20)
            total_hours += x

        # Print the total amount of both full time and part time staff
        print("Total yearly earnings of temps and full time staff are: ", total_hours + full_time_hours)
        print("Average wage per staff member is: ", (full_time_hours + total_hours) / (how_many + y))

    # The total of just full time staff
    else:
        print("Average wage per staff member is: ", full_time_hours / y)
        return print("Total yearly wage is: ", full_time_hours)


full_time(y)