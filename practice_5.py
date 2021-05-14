#encrypting password

def crypt(password):
    encryption= " "
    for element in password:

        if element in "Aa":
            encryption= encryption + "."
        elif element in " ":
            encryption= encryption + "."
        elif element in "Bb":
            encryption= encryption + "."
        elif element in "Cc":
            encryption= encryption + "."
        elif element in "Dd":
            encryption= encryption + "."
        elif element in "Ee":
            encryption= encryption + "."
        elif element in "Ff":
            encryption= encryption + "."
        elif element in "Gg":
            encryption= encryption + "."
        elif element in "Hh":
            encryption= encryption + "."
        elif element in "Ii":
            encryption= encryption + "."
        elif element in "Jj":
            encryption= encryption + "."
        elif element in "Kk":
            encryption= encryption + "."
        elif element in "Ll":
            encryption= encryption + "."
        elif element in "Mm":
            encryption= encryption + "."
        elif element in "Nn":
            encryption= encryption + "."
        elif element in "Oo":
            encryption= encryption + "."
        elif element in "Pp":
            encryption= encryption + "."
        elif element in "Qq":
            encryption= encryption + "."
        elif element in "Rr":
            encryption= encryption + "."
        elif element in "Ss":
            encryption= encryption + "."
        elif element in "Tt":
            encryption= encryption + "."
        elif element in "Uu":
            encryption= encryption + "."
        elif element in "Vv":
            encryption= encryption + "."
        elif element in "Ww":
            encryption= encryption + "."
        elif element in "Xx":
            encryption= encryption + "."
        elif element in "Yy":
            encryption= encryption + "."
        elif element in "Zz":
            encryption= encryption + "."
        else:
            encryption= encryption+element
    return encryption


print(crypt(input("enter password:")))

