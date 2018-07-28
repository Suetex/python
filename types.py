c=complex(1,-2)
c.conjugate()
print c

a=[1,2,3,"n"]# type'list':can be changed
b=["i","am",5,6]
c=(1,2,3)# type'tuple':can't be changed
print a[0],a[3]
print b[0],b[2]
a[1]="k"
print a[1]# index must be in []

d=range(3)
e=range(0,10,2)
print d,e

#f="apple"
#f[1]="b"
#print f# can't be changed

things="apple orange banana grape pear"
stuff=things.split(' ')
print stuff
print' '.join(stuff)


