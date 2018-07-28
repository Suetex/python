from sys import argv
script,textfile=argv
text=open(textfile,'r+')
line1="the answer to the life,the universe and everything"
text.write(line1)
text.write("\n")
text.write("42")


