# excercises 22 and 23 did not involved writing any new files. 
# so it is not that I or Zed lost count, we are simply counting things other than these files.

print "I'm going to practice everything that we've used in this book so far"
print 'You think I\'d \'bout escapes with \\ by know and how to make \nnewlines and \n\ttabs'

poem = """
\tThe lovely world
with logic is so firmly planted
in my mind. It cannot discern the \nneeds of love
nor comprehend passion from intuition and requires
an explanation
\n\t\twhere there is none.
"""
def drawLines():
    for i in range(1,6):
        print "----------------\n"
        
drawLines()
print poem
drawLines()

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 1000
    crates = jars / 100
    return jellyBeans, jars, crates
    
startPoint = 10000
beans, jars, crates = secret_formula(startPoint)

print "With a starting point of: %d" % startPoint
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(startPoint)

startPoint = startPoint/10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(startPoint)

