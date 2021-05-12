
#creating and blocking a password (while loop)
password = "toludoyin"
enter_password = " "
number_of_try = 0
maximum_number_of_try = 3
maximum_try = "not reached"

while enter_password!=password and maximum_try!="Reached":
    if number_of_try<maximum_number_of_try:
        enter_password = input("What is your password:")
        number_of_try=number_of_try+1
    else:
        maximum_try="Reached"

if maximum_try =="Reached":
    print("account blocked")
else:
    print("processing")



   



