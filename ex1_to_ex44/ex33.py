i = 0
numbers = []

while i < 6:
    print "At the top the i is %d" % i
    numbers.append(i)
    
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for j in numbers:
    print j
