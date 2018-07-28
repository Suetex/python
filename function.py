def print_none():# with a : behind
 print"hello world"# must have an indent
def print_one(arg1):
 print"i like %s"%arg1
def print_two(arg1,arg2):
 print"i like %r and %r"%(arg1,arg2)
print_none()
print_one("banana")
print_two("banana","peach")

def add(a,b):
 return a+b
groupA=20
groupB=30
total=add(groupA,groupB)
print"total is %d"%total


def cuboid(a,b,c):
 S=a*b
 return S*c# the lines indented r all in the function area
a=2
b=3
c=4
print"%d"%cuboid(a,b,c)
 
