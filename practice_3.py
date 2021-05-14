 #for loop

onelevel = ["maths","science"]
twolevel = ["economics","statistics"]
threelevel = ["industrial","macroeconomics"]
fourlevel = ["econometrics", "applied statistics"]

for o in onelevel:
    for t in twolevel:
        for th in threelevel:
            for f in fourlevel:
                print("In economics department,we have the above courses for each level, 100:" + o +  "also 200:"  + t + "cum 300:" + th + "and 400:" + f)



