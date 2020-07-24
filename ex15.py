from sys import argv

script,filename=argv #take the input i.e. file name through argv

txt=open(filename) #open command is used to open the file 

print(f"here's your file {filename}:") #print the variable value of filename
print(txt.read())   #read the content in txt variable using read function

print("type the filename again:")
file_again=input(">")

txt_again=open(file_again)

print(txt_again.read())
