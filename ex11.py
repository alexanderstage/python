# need spaces after the strings so that the answer reads correctly
name = raw_input("What is you name? ")
print "Hello, %s." % name

residence = raw_input("Where are you from? ")
print "Ah, you are from %s" % residence

# Convert the string to an integer using int()
age = int(raw_input("How old are you? "))
print "You are %d years old" % age

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

# Print a list of the details inputted
print '''
Here are the details you gave us:
\t* you're name is %s 
\t* you are %d years old, 
\t* you're %s tall, 
\t* you are %s heavy
\t* you come from %s.
''' % (name, age, height, weight, residence)