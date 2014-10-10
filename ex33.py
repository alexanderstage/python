


def myloop(max, inc):
    i = 0
    numbers = []

    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

myloop(10, 1)