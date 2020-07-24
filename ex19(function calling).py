def cheese_and_crackers(cheese_count,crackers_count): #function defination start ith def end with:
    print(f"If u have {cheese_count} cheeses.!") #indent space
    print(f"If u have {crackers_count} crackers.!")
    print("Man that's enough for a party..!!")
    print("\nGet a blanket.\n")

print("we can just give the functons numbers directly: ")
cheese_and_crackers(20,30) #calling function by directly passing values.

print("OR we can use variables from our script:")
amount_of_cheese=10         #temporory varibles to pass value to function
amount_of_crackers=20
cheese_and_crackers(amount_of_cheese,amount_of_crackers) #passing value to function using temp varibles or from script

print("We can do math inside too:")
cheese_and_crackers(10+20,5+6)

print("and we can combine two, varibles and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
