list1=[1,2,3,'a','b','c']
list2=[5,6]
tuple1=(1,2,3,'a','b','c')
a='a' in list1
b='a' not in tuple1
c=list1+list2
d=list1*2
e=list1[0:2]
f=list1[0:5:2]
g=len(list1)
h=min(list1)
i=max(list1)
j=list1.count('a')
k=list1.index(3,0,4)
print a,b,c,d,e,f,g,h,i,j,k


#del list1[0:5:2]
#print list1
#del list1[0:2]# not contain list1[2] but contain[0]
#list1[0:3:1]='k'#????
list1.append('d')
print list1



