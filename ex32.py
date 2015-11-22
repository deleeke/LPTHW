the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goes through a list
for i in the_count:
    print "This is the count %d" % i

for j in fruits:
    print "A fruit of type: %s" % j 

# we can have mixed lists too
for i in change:
    print "I got %r" % i
    
# we can also build lists
elements = []

# then use the range funciton to do 0 to 5 counts:
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print "Element was: %d" % i
