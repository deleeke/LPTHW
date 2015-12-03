print """
You enter a dark room with two doors barely lit by the glowing 
eyes of a million wolf spider babies that crawl 
like a sea of lights on the floor. 
Do you go through door #1 or door #2?
"""
door = raw_input("> ")

while door != '1' and door != '2':
    print "(Please enter either 1 or 2)"
    door = raw_input("> ")
        
if door  == "1":
    print "There's a giant bear here eating a cheese cake."
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    while bear != '1' and bear != '2':
        print "(Please enter either 1 or 2)"
        bear = raw_input("> ")
    
    if bear == '1':
        print "The bear eats your face off. Good job!"
    elif bear == '2':
        print "The bear eats your legs off. Good job!"

elif door == '2':
    print 'You stare into the endless abyss at Cthulu\'s retina.'
    print '1. Blueberries.'
    print '2. Yellow jacket clothespins.'
    print '3. Understanding revolvers yelling melodies.'
    
    insanity = raw_input("> ")
    
    if insanity == '1' or insanity == '2':
        print 'Your body survives powered by a mind of jello. Good job!'
    else:
        print 'The insanity rots your eyes into a pool of gummy bears. Good Job!'
