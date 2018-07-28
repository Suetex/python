from sys import argv
script,circum_input=argv
circum_input=float(circum_input)

pi=3.14
rearth=6371
rmars=3397
r_input=circum_input/(2*pi)
r_input=int(r_input)

if r_input<=6380&r_input>=6350:
 print "it's earth"
elif r_input<=3410&r_input>=3390:
 print"it's mars"
elif r_input<=6391&r_input>=6351:
 print"it' close to the earth"
elif r_input<=3417&r_input>=3377:
 print"it' close to the mars"
else:
 print"the data is neither earth or mars,please check it again"
