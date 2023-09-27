def write_line():
    f = open("/Users/milesjones/Documents/PROG_1/test.txt","w")
    f.write("Hello World")


def read_files_by_line():
    f = open("/Users/milesjones/Documents/PROG_1/test.txt","r")
    line_one = f.readline()
    print(line_one)

write_line()
read_files_by_line()