def Party(cheeseCnt, crackersCnt):
    print """
    You have %d cheeses and %d crackers.
    Hot diggity, that's enough for a Party!
    Get a blanket.\n
    """ % (cheeseCnt, crackersCnt)

print "We can just give the function numbers directly:"
Party(100, 200)

print "OR, we can use variables from the script"
usrCheese = int(raw_input("How much cheese do you have?\n>"))
usrCrackers = int(raw_input("How many boxes of crackers do you have?\n>"))

Party(usrCheese, usrCrackers)

print "We can even do math inside"
Party(10+100, 5+400)

print "And we can combine variables and input and math:"

usrCheese = int(raw_input("How much cheese do you have?\n>"))
usrCrackers = int(raw_input("How many boxes of crackers do you have?\n>"))

Party(usrCheese+1000, usrCrackers+100)

