
economics_grade = {'applied statistic': 78,
 'econometrics': 93,
 'economic planning': 85}


print( economics_grade.items())

print(type(economics_grade))

print(len(economics_grade))

economics_grade.update({'project evaluation': 81, 'advanced macro': 100 ,'economics system':70})
print(economics_grade.items())

economics_grade.pop('economics system')
print(economics_grade)

if 'economics system' in economics_grade:
  print(True)
else:
    print(False)

new_economics_grade = economics_grade ['applied statistic']+4
print(new_economics_grade)


econometrics = economics_grade['econometrics']
print('the highest mark is {} econometrics, of the name zee'.format(econometrics))


