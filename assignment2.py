#dictionaries
economics_grade = {
    'Applied statistics': 78,
    'Econometrics': 100,
    'Comparative economics' :74,
    'Economics planning' :90,
    'Project evaluation1' : 79
}
print(type(economics_grade))

economics_grade2 = {
    'Applied statistics2': 88,
    'Econometrics2': 73,
    'Comparative economics2' :86,
    'Economics planning2' :80,
    'Project evaluation2' :72,
    'Project evaluation3' : 81
}

economics_grade1= economics_grade.copy()
economics_grade1.update(economics_grade2)
print(economics_grade1)

economics_grade.update(
    {
        'Project ': 81,
        'Project evaluation' :99,
        'Macroeconomics' :89,
        'Applied statistics' :82
    })
economics_grade['Analysis'] = 78
                   #2
economics_grade.pop('Project evaluation1')
print(len(economics_grade))
print(sorted(economics_grade, reverse=True))
print(sum(economics_grade.values()))
print(sorted(economics_grade1.items()))

if 'economics system' in economics_grade:
  print(True)
else:
    print(False)

for a in economics_grade.items():
    print(a)

Econometrics = economics_grade['Econometrics']
print('The highest mark is {} Econometrics, of the name zee'.format(Econometrics))



# MULTIPLE VARIABLE
fruits = ["Banana","Orange","Pineapple","Apple"]
A,B,C,D = fruits
print(A)
print(B)
print(C)
print(D)


#GLOBAL VARIABLE
x = "expression"

def analysis():
     x = "statistics"
     print("The name of my analysis is" + x)

analysis()

print("The name of my analysis is" + x)

x = "expression"
def analysis():
    global x
    x = "statistics"

analysis()

print("The name of my analysis is" + x)


#FOR and WHILE LOOP
A=2
while A < 40:
    print(A)
    A +=2

a=4
while a <40:
    print(a)
    if a ==26:
        break
    a +=4


#FOR LOOP
fruits = ["Banana","Orange","Pineapple","Apple"]
for x in fruits:
    print(x)
    if x == "Pineapple":
        break

fruits = ["Banana","Orange","Pineapple","Apple"]
for x in fruits:
    if x == "Pineapple":
        break
    print(x)

fruits = ["Banana","Orange","Pineapple","Apple"]
for x in fruits:
    if x == "Orange":
        continue
    print(x)

fruits = ["Banana","Orange","Pineapple","Apple"]
for x in "Banana":
    print(x)

for a in range(6 , 37, 4):
    print(a)
else:
    print("Finally done")

for a in range(50 , 101):
    print(a)

names = ["manny","roland","okiki","alfred"]
courses= ["maths","eng","econs","agric"]
for a in names:
    for b in courses:
        print(a,b)

#FUNCTION
def biography(fname,lname):
    print("My name is " + fname + " " + lname)

biography("Toludoyin" , "Shopein")


# #ARBITRARY ARGUEMENT
def houses(*keys):
    print("This house belongs to" + " "+ keys[3])
houses("don","ken","mia","shab","manny")

def admission(*name):
    print("my preferred institution is Crawford University and my name is" +
    " " + name[2])
admission("temi","tolu","doyin","feyi","femi","esther")


# #KEYWORD ARGUEMENT
def children(child1,child2,child3,child4):
    print("my name is" + child3 + "and i live in a duplex")

children(child1="racheal",child2="bimpe",child3="folu",child4="murry")

def name(state1,state2,state3,state4,state5,state6):
    print("this is our lovely key to the house in" + state1)
name(state1= "Dubia", state2="Jarmany",state3="Ethopia",state4="USA",state5="Autraillia",state6="Ghana")


# #ARBITRARY KEYWORD ARGUEMENT
def name(**kid):
    print("my firstname is" + kid["fname"] + "and my lastname is" + kid["lname"])
name(fname= "doyin",lname="shopein")

def name(**state):
    print("this is our lovely key to the house in" + state["state1"])
name(state1= "Dubia", state2="Jarmany",state3="Ethopia",state4="USA",state5="Autraillia",state6="Ghana")


#DEFAULT PARAMETER VALUE
def country(state="Ogun"):
    print("I am from"+ state)

country(state="Abia")
country(state="Anambra")
country()
country(state="Yobe")
country(state="Borno")











