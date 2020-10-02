def get_file_lines(filename):
    poem = "poem.txt"
    infile = open(poem, "r").readlines()
    infile.close()
    return infile

def lines_printed_backwards(lines_list):
    lines_list = open("poem.txt", "r").readlines()
    num_of_lines = len(lines_list)
    lines_list = lines_list.reverse()

    for line in range(num_of_lines):
        reverse = str(num_of_lines - line) + "" + lines_list[line]
        print(reverse)