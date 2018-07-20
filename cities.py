#A program introducing usage of dictionaries with usage and key and value pair and different way of interpretating data within

# create a mapping of state to abbrevation
states = {'Oregon' :'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}

# create a basic set of states and some cities in them
cities = {'CA':'San Fransico','MI' : 'Detroit','FL' : 'jacksonville'}

# add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print ('- ' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR']) 

# print some states
print ('-'*10)
print("Michigan's abbreviation is ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#print every state and abbreviations
print ('-'*10)
for states,abbrev in states.items():
    print("%s has the city %s" % (states,abbrev))

#print every city in state 
print('-' *10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))


# now do both at the same time
print('-' * 10)
for states,abbrev in states.items():
    print("%s state is abbreviated as %s and has city %s" % (states, abbrev))


