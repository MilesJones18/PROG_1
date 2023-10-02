

def feet_to_inches(feet):
    inches = feet * 12
    print(f"{inches} inches")
    return inches


if __name__ == "__main__":
    user_input = int(input("Please enter the number of feet: "))
    feet_to_inches(user_input)