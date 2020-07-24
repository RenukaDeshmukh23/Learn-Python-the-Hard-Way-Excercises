print("Let's practice everything.")
print('You\'d nedd to know \'bout escapes with \\ that do: ') #\ to escape the '
print('\n newlines and \t tabs.')

poem = """
\t the lovely world
with logic so firmly planted
cannot descern \n the needs of love
\n\twhere there is none.
"""

print("-----------")
print(poem)
print("-----------")

five = 10-2+3-6                         #calculations
print(f"this should be five:{five}")    #print stat using f

def secret_formula(started):        #def_keyword function_name (argument)
    jelly_beans = started*500       #function variables
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars , crates

start_point = 10000
beans, jars,crates = secret_formula(start_point)

#another way to format a string
print("with starting point of :{}".format(start_point))
#now with f "" string
print(f"we'd have {beans} beans,{jars} jars and {crates}crates")

start_point=start_point/10

print("we can also do that this way:")
formaula= secret_formula(start_point)
#easy way to apply list to a format string
print("we'd have {} beans,{} jars, and {} crates.".format(*formaula))
