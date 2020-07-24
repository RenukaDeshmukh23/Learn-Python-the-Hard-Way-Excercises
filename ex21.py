def add(a,b):
    print(f"Adding {a}+{b}")
    return a+b

def sub(a,b):
    print(f"Subtracting {a}-{b}")
    return a-b

def mul(a,b):
    print(f"Multipying {a}*{b}")
    return a*b

def div(a,b):
    print(f"Dividing {a}/{b}")
    return a/b

print("Let's do some math ...")

age=add(30,5)
weight=sub(80,20)
height=mul(20,4)
iq=div(100,5)

print(f"\nAge:{age} , Height:{height} , Weight={weight} , Iq:{iq}")

print("\nPuzzle here\n")

what=add(age , sub(height,mul(weight, div(iq,2))))

print("That becomes :", what , "can you do it ?")
