ten_things = "apples oranges crows telephone light sugar"

print("Wait there are not 10 things in list.. Let's fix that..!!")              #print the statement

stuff = ten_things.split(' ')                                                   #assign the list ten_things to stuff with ''
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]      #more_stuff another list

while len(stuff) != 10:                                                         #while loop len to count the length=10
    next_one = more_stuff.pop()                                                 #add the item from more_stuff
    print("Adding:",next_one)                                                   #print which item is getting added
    stuff.append(next_one)                                                      #using append value at next_one is added in stuff list
    print(f"There are {len(stuff)} items now.")                                 #print length of stuff list

print("There we go:",stuff)                                                     #print all items in list stuff

print("Let's do some things with stuff.")                                       #print the statement

print(stuff[1])                                                                 #print the value at 1 from stuff list
print(stuff[-1])                                                                #
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
