from sys import argv
script,textfile1,textfile2=argv
text1=open(textfile1,'w+')
text2=open(textfile2,'w+')
line1="i have a cat"
line2="his name is pudding"
text1.write(line1)
text1.write("\n")
text1.write(line2)
text1.seek(0,0)
text2.write(text1.read())
text2.seek(0,0)
print text2.read()
