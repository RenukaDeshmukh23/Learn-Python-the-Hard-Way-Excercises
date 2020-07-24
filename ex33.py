i = 0                                   #intialise to 0
numbers = []                            #empty list numbers

while i<6:                              #while loop started
    print(f"At the top i is {i}")       #print the value of i
    numbers.append(i)                   #append will add value of i to numbers list

    i=i+1                               #increase the value of i
    print("Numbers now:",numbers)       #print the contents of numbers list
    print(f"At the bottom i is {i}")    #print the value of i after i+1

print("The numbers:")                   #after end of loop print the contents in numbers list

for num in numbers:                     #start of for loop
    print(num)                          #print the values in list
