from sys import argv
from time import sleep

script, filename = argv

print "We're going to erase the contents of %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("? >")

print "Opening the file...\n"
target = open(filename, 'w')
sleep(1)

sleep(1)
print "Now I'm going to ask you for three lines.\n"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file.\n"

target.write(line1+"\n"+line2+"\n"+line3+"\n")

sleep(1)

print "Now I'm going to close the file to save it and then open it again.\n"
sleep(1)

target.close()
target = open(filename)

print "Lets check out what that looks like:\n"
sleep(1)
print target.read()
