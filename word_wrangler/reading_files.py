FILENAME = "examples_files_dracular.txt"

file = open(FILENAME, 'r')

print type(file)

for line in file.readlines():
    print line[:-1] #strip out the extra line feed on the end of every line