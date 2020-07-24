from sys import argv

script,fileName=argv

print(f"we are going to erase {fileName}.") #format the statement(i.e. add value of fileName &) print
print("If u don't want that ,hit CTRL-C (^C).")#print
print("If u do want that ,hit RETURN.")#print

input("?")#print '?' and store the input from user.
print("opening the file...")
target=open(fileName,'w')
print("Truncating th file.Goodbye..!!")
target.truncate()

print("Now i'm going to ask you for three lines.")
line1=input("line1: ")
line2=input("line2: ")
line3=input("line3: ")

print("I'm going to write these to the file..")

target.write(line1) #write the line1 in the file whose address is stored at target variable.
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it.")
target.close() #close function to close the file 
