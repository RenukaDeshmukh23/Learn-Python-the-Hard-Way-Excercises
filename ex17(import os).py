from sys import argv
from os.path import exists #exists will return true or false depending on existence of file in folder.

script,from_file,to_file=argv #3 argv arguments declared

print(f"Copying from {from_file} to {to_file}") #by formatting print the stat.

in_file=open(from_file) #open() will open file stored @ From_file assign it to in_file.
indata=in_file.read() #read() to read the contents assign the value to indata variable.

print(f"The input file is {len(indata)} bytes long") #len to count length of file

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue,CTRL-C to abort.")
input()

out_file=open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
