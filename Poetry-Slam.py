import random

def get_file_lines(filename):
    poem = "poem.txt"
    infile = open(poem, "r").readlines()
    infile.close()
    return infile

def lines_printed_backwards(lines_list):
    lines_list = open("poem.txt", "r").readlines()
    num_of_lines = len(lines_list)
    lines_list = lines_list[:: -1]

    for line in range(num_of_lines):
        reverse = str(num_of_lines - line) + "" + lines_list[line]
        print(reverse)

def lines_printed_random(lines_list):
    lines_list = open("poem.txt", "r").readlines()
    num_of_lines = len(lines_list)
    
    for line in lines_list:
        line = random.randrange(num_of_lines)
        random_order = str(line + 1) + "" + lines_list[line]
        print(random_order)

def lines_printed_custom(lines_list):
    lines_list = open("poem.txt", "r").readlines()
    num_of_lines = len(lines_list)
    i = 1

    for i in range(num_of_lines):
        if i % 2 == 0:
            print(i,lines_list[i])
        i += 1