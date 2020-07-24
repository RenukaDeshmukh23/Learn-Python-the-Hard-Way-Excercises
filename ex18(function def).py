def print_two(*args):    #def creates the function "print_two" and (*args) is argument
    arg1,arg2=args      #indenting space
    print(f"arg1:{arg1} arg2:{arg2}") #it will print values of arg1 and arg2

def print_two_again(arg1,arg2):  #end the line with :
    print(f"arg1:{arg1} and arg2:{arg2}")

def print_one(arg1):   #passing only one argument arg1
    print(f"arg1:{arg1}")

def print_none():  #passing zero argument
    print("I got nothing")

#function callimg
print_two("abc1","abc2")
print_two_again("abc1","abc2")
print_one("abc..!!")
print_none()
