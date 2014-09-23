# Function that takes 2 arguments and prints the results of the values that are passed to it
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Prints the amount of cheeses based on the value passed to 'cheese_count'
	print "You have %r cheeses" % cheese_count
	# Prints the amount of crackers based on the value passed to 'boxes_of_crackers'
	print "You have %r boxes of crackers" % boxes_of_crackers
	# Prints a string
	print "Man that's enough for a party!"
	# Prints a string
	print "Get a blanket.\n"

print "We can just give the function numbers directly"
# Runs the function passing 2 values to it 
cheese_and_crackers(20, 30)

print "Or we can use variables from our scripts:"
# Create 2 variables
amount_of_cheese = 10
amount_of_crackers = 50

# Runs the function passing it the two variables 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too."
# Runs the function passing it 2 varibles that we use math to create
cheese_and_crackers(10 + 20, 5 + 6)

print "and we can combine the two, variables and math:"
# Runs the function 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)