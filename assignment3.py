#global keyword
x="Tolani"
def result():
    global x
    x="Bimbo"
    print("my name is",x)
result()

print("my name is",x)

#looping string
for x in "money":
    print(x)


name=["soji","taiwo","kemi","bimbo"]
name1=["dami","mary","success"]
name.extend(name1)
print(name)

name=["soji","taiwo","kemi","bimbo"]
for x in range(len(name)):
    print(name[x])

#using while loop for list
name=["soji","taiwo","kemi","bimbo"]
s= 0
while s < len(name):
    print(name[s])
    s= s+1

name=["soji","taiwo","kemi","bimbo"]
[ print(x) for x in name]

#list comprehension
name=["soji","taiwo","kemi","bimbo"]
newlist=[n.upper() for n in name if "m" in n]
print(newlist)

sample=[a for a in range(12)]
print(sample)

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

