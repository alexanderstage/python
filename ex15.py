# Imports the 'argv' module
from sys import argv

# unpacks the argv module
script, filename = argv

# opens a file using the variable filename (input by the user)
# and asigns it to the variable txt
txt = open(filename)

# Prints out a message with the title of the file in it
print "Here's your file %r:" % filename
# Prints the contents of the file calling the read() function on 'text'
print txt.read()

# Close the file now that is has been used
txt.close()

# Prints a prompt for the user to enter the filename again
print "Type the filename again:"
# Assigns the variable input to a variable
file_again = raw_input("> ")

# Opens the file and assigns it to a variable
txt_again = open(file_again)

# Prints out the contents of the file again
print txt_again.read()

# Close the file now that is has been used
txt.close()