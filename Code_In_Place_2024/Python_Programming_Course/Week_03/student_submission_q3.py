def is_within_range(number, start, end):
    return start <= number <= end
try:
    number = int(input("Enter the number to check: "))
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if is_within_range(number, start, end):
        print(f"{number} is within the range of {start} to {end}.")
    else:
        print(f"{number} is not within the range of {start} to {end}.")
except ValueError:
    print("Invalid input. Please enter valid integers.")