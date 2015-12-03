ten_things = "Apples Oranges Cows Bugs Telephone Light Sugar"

print "Wait there are not 10 things on that list. Let's fix that. "

stuff = ten_things.split()
more_stuff = "Day Night Song Frisbee Corn Banana Monkey Supersoaker".split()

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # counting from the end
print stuff.pop()
print " ".join(stuff)
print "#".join(stuff[4:8])
