# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

line = '-'*10

# print out some cities
print line
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Print some states
print line
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Do it by using the state then the cities dict
print line
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print line
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in states
print line
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do it both at the same time
print line
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])

print line
usr_state = str(raw_input("Enter a state you'd like to know more about > "))

# safely get abbreviation by state by state that might not be there
state = states.get(usr_state)

if not state:
    print "Sorry, no %s." % usr_state

else:
    #get a city with a default value
    city = cities.get(states[usr_state])
    print "The city for the state %s is: %s" % (states[usr_state], city)
