#global keyword
x="Tolani"
def result():
    global x
    x="Bimbo"
    print("my name is",x)
result()

print("my name is",x)


name=["soji","taiwo","kemi","bimbo"]
name1=["dami","mary","success"]
name.extend(name1)
print(name)

#acsending and descending order
name=["soji","taiwo","kemi","bimbo"]
name.sort(reverse=True)
print(name)

#tuple
name= ("james","ore","femi","sade")
if "doyin" in name:
    print("not in")
else:
    print("found")
print(type(name))
print(name[:-1])

#to change a tuple
name= ("james","ore","femi","sade")
name1= list(name)
name1[3]= "rayo"
name= tuple(name1)
print(name)

name= ("james","ore","femi","sade")
name1= list(name)
name1.append ("rayo")
name= tuple(name1)
print(name)

#using asterisks
name= ("james","ore","femi","sade")
(level1,*level2,level3)= name
name1= list(name)
name1.remove ("ore")
name= tuple(name1)
print(level1)
print(level2)
print(level3)

