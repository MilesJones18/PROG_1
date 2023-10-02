def format_file():
    formatted_file = open(f"/Users/milesjones/Documents/PROG_1/File2.txt",'w')

    with open(r"/Users/milesjones/Documents/PROG_1/File1.txt",'r') as file:

        for lines in file:
            if not lines.isspace():
                formatted_file.write(lines)


if __name__ == "__main__":
    format_file()