formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","Two","Three","Four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
"try your",
"own text here",
"maybe a poem",
"some text missing"
))


#in this program we have declared the 'formatter' variable with 4 {}
#then various print statements are involed printing various values like
#numbers, string,true-false, then the formatter variable itself used
#which will print for 1 formatter 4{} so 16 {}
#then we have given 4 text lines to print
