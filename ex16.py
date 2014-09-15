
# Imports the argument variable from the 'sys' package
from sys import argv

# Unpacks teh argv
script, filename = argv

# Just prints out some instructions on how to use a terminal
print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# prompts for user input
raw_input("?")

print "Opening the file..."
# Opens the file in write mode
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# deletes the contents of the file
target.truncate()

print "Now i'm going to ask you for three lines."

# Prompts for text input and assigns it to 3 variables
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to a file."

# Assigns the contents from the 3 variables to the 'writeline' with 3 line breaks
writeline = "%s\n%s\n%s\n" % (line1, line2, line3)

# Adds the contents to the file
target.write(writeline)

print "And finally, we close it."
# Closes the file
target.close()