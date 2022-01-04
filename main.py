# Write a Program to copy a text file to another file 

f=open("file.txt","w")
f.write("this is python lab")
f.close()
f=open("file.txt","r")
c=open("file2.txt","w")
for n in f:
  c.write(n)
f.close()
c.close()


