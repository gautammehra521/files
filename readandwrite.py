#write function is used to erite into the text file
f=open("C:\\Users\\Gautam\\Desktop\\read and write files python\intern.txt","w")
f.write("hello,i love coding\n I am a intern in itintern")
print("created the text file")
print("I wrote successfully")

#append function as it rewrite the new file
f=open("C:\\Users\\Gautam\\Desktop\\read and write files python\intern.txt","a")
f.write("hello,i love python\n I am a intern in itintern")
print("created the text file")
print("I wrote successfully")
print("I append the file")

#reading a file line by line
f=open("C:\\Users\\Gautam\\Desktop\\read and write files python\intern.txt","r")
print(f.read())
f.close()
print("I read successfully")
print("File is now closed")

#count number of wrords and reading lione by line
f=open("C:\\Users\\Gautam\\Desktop\\read and write files python\intern.txt","r")
for line in f:
    Tokens=line.split(" ")
    print(len(Tokens))
print(line)
f.close()


#word count in python
f=open("C:\\Users\\Gautam\\Desktop\\read and write files python\\intern.txt","r")
f_new=open("C:\\Users\\Gautam\\Desktop\\read and write files python\\newintern.txt","w")

for line in f:
    Tokens=line.split(" ")
    f_new.write("wordcount"+str(len(Tokens))+line)

f.close()
f_new.close()

#file with statements 
with open("C:\\Users\\Gautam\\Desktop\\read and write files python\\intern.txt","r") as f:
print(f.read())
print(f.closed)