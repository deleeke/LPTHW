import hashmap

line = '-'*10

# create a mapping of state to abbrevation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL') 
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print some cities
print line
usr_state = str(raw_input("Enter a state to find out cities that are located there.\n> "))
usr_abbrv = hashmap.get(states, usr_state)
print "%s State has: %s" % (usr_state, hashmap.get(cities, usr_abbrv))

# print every state abbreviation
print line
hashmap.list(states)

# print every city in states
print line
hashmap.list(cities)

print line

usr_state = str(raw_input("Enter a state you'd like to know more about\n> "))

state = hashmap.get(states, usr_state)

if not state:
    print "Sorry, no %s." % usr_state


