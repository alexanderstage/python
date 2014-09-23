# import argv from the sys module
from sys import argv

# unpack argv
script, input_file = argv

# function that accepts one parameter
def print_all(f):
	# print the contents of the file passed to the function 
	print f.read()

# function that accepts one parameter
def rewind(f):
	# find the start (line 0) of the file passed to the function
	f.seek(0)

# function that accepts two parameters 
def print_a_line(line_count, f):
	# use the line count passed to the function to print the
	# content of the line the script is currently on 
	print line_count, f.readline()

# open the file passed to the script and assign it to a variable 
current_file = open(input_file)

# print a string that ends with a line break
print "First lets print the whole file.\n"

# run the print_all function, passing it the opened file 
print_all(current_file)

# print a string
print "Now lets rewind, kind of like a tape."

# run the rewind function, passing it the opened file
rewind(current_file)

# print a string
print "Lets print three lines:"

# assign a value to the 'current_line' variable
current_line = 1
# run the print_a_line function passing it the current line number
# and the opened file
# Current line = 1
print_a_line(current_line, current_file)

# increase the line number by 1
current_line += current_line
# run the print_a_line function passing it the current line number
# and the opened file
# current line = 2
print_a_line(current_line, current_file)

# increase the line number by 1
current_line += 1
# run the print_a_line function passing it the current line number
# and the opened file
# current line = 3
print_a_line(current_line, current_file)