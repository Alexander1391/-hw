
day = '05.17.2016'
s = day.split('.')
zerofive = s[0]
s[0] = s[1]
s[1] = zerofive

print(".".join(s))


name = "Mark Zuckerberg"
adc = name.split()
adc[0], adc[1] = adc[1], adc[0]
print(" ".join(adc))

s = 'employee_first_name'
case = s.split('_')
case[0] = case[0].title()
case[1] = case[1].title()
case[2] = case[2].title()
print("".join(case))



s = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = s.split("*")
name = lst[0]
birthday = lst[1]
finishDate = lst[2]
birthdayYear = birthday.split('-')[0]
finishYear =  finishDate.split('-')[0]
age = int(finishYear) - int(birthdayYear)
data = name, age
print(data)







