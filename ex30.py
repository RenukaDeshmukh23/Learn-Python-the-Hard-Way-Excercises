people = 60
cars = 40
trucks = 10

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")

if trucks > cars:
    print("that's too many trucks")
elif trucks < cars:
    print("may be we could take the trucks")
else:
    print("we still can't decide")

if people > trucks:
        print("alright,let's just take the trucks")
else:
        print("Fine,let's stay home then")
