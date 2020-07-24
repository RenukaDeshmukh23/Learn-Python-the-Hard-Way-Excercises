#create a mapping of state to abbrevations
states = {
    'oregon':'OR',                                                              #VAlues : Keys
    'Florida':'FL',
    'California':'CA',
    'NewYork':'NY',
    'Michigan':'MI'
}
#create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
    }
#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print some cities
print('-'* 30)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])

#print some states
print('-'* 30)
print("Michigan's abbrevation is:",states['Michigan'])
print("Florida's abbrevation is :",states['Florida'])

#do it by using the states then cities dict
print('-'*30)
print("Michigan has :",cities[states['Michigan']])
print("Florida has :",cities[states['Florida']])

#print every state abbrevation:
print('-'*30)
for state, abbrev in list(states.items()):
    print(f"{state} is abbriviated {abbrev}")

#print every city in state
print('-'*30)
for abbrev , city in list (cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at same time
print('-'*30)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbriviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*30)
#safetly get the abbrevation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry no Texas")

#get a city with a default value
city = cities.get('TX','Does not exist')
print(f"The city for the state 'TX' is {city}")
