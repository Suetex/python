from sys import argv
script,name,radius=argv
r=float(radius)
def circum(r):
 pi=3.14
 return 2*pi*r
print"the circumference  of %s is %f"%(name,circum(r))

def dec(a,b):
 return a-b
a=raw_input("input the first number : ")
a=float(a)
b=raw_input("input the second number : ")
b=float(b)
print"the difference between the two number is %f"%dec(a,b)
