# -*-coding:utf8
# http://learnpythonthehardway.org/cook/ex39.html

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Hawaii': 'HI',
}

# create a basis set of states and some oities in them
cities = {
    'CA': 'Los Angeles',
    'HI': 'Honolulu',
    'FL': 'Orlando',
}

# add some more oities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some oities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

# print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

# print some states
print('-' * 10)
print("states = %s" % states)
print("states.items() = %s" % states)
print('-' * 10)
for state, abbrev in states.item():
    print("%s is abbreviated %s")

# print every city in state
print('-' * 10)
for abbrev, city in cities.item():
    print("%s has the city %s" % states)

# now do both at the same time
print('-' * 10)
for state, abbrev in states.item():
    print("%s state is abbreviated %s and has city %s" %(
        state, abbrev, cities[abbrev]
    ))

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry no texas yet.")

# get a city with a default value
city = cities.get('TX', 'Not Entered Vet')
print("The city for the state 'TX' is: %s" % city)

# 여기까지 입력 후 add. commit  # 각 행 주석 입력 후 commit