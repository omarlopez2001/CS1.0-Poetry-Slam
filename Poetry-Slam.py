def get_file_lines(filename):
    poem = "Poem.txt"
    infile = open(poem, "r").readlines()
    infile.close()
    return infile