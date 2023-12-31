'''Take a users input of time in seconds, plugs it into the formula d = 0.5 * 9.8 * t^2, where t is the users input. 
    Then, iterates through each second and prints out the distance traveled in meters.'''


user_time = int(input("Please enter the time in seconds: "))  # First and foremost gets the users input.


def formula(time):  # This function is the formula for the distance traveled.
    answer = 0.5 * 9.8 * (time ** 2)
    return answer


def loop():
    for sec in range(1, user_time + 1):  # Iterates from 1 to the user inputted time and calls the formula function.
        print(f"{sec} seconds: {formula(sec):.1f} meters")  # Prints each iteration of the loop.


if __name__ == "__main__":
    loop()

