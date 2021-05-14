
def econ_dept():
    name= input("Enter full name in the box below:").upper()

    result = input("enter your level, 100, 200, 300, 400:")
    if result==str(100-400):
        return print("fill in the space for your level:")

    else:
        print("processing")

        result_1= input("rain or harmattan semester?")
        if result_1!="rain":
            return print("webpage not loading")
        else:
            print(result,"level rain semester result" )

econ_dept()




def game():
    intro= input("Welcome to tiktaktok")

    intro_1=input("Click start or end to begin (start/end):")
    if intro_1!="start":
        return print("return home")
    else:
        print("let's begin")

game()




def purchase():
    market=input("Welcome").upper()
    market1=input("To begin purchase,register your name:")
    market2=input(" Register your card to purchase multiple product instantly")
    market3=input("Goods available are in market4,to check go to markert4, to stop press back (market4 or back):")
    if market3!="market4":
        return print("return to dashboard")
    else:
        print("goods sold on this network include;clothes,sneakers,shoes,slippers")


purchase()


x=1
while x<10:
    print(x)
    x=x+1

level100=("teni,temi,bunmi,sola,taiwo,doyin,wale,talabi")
for level100s in level100:
    print(level100s)