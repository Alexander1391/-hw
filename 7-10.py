
day = '05.17.2016'
s = day.split('.')
day = s[0]
s[0] = s[1]
s[1] = day

print(".".join(s))


name = "Mark Zuckerberg"
conversely = name.split()
conversely[0], conversely[1] = conversely[1], conversely[0]
print(" ".join(conversely))

s = 'employee_first_name'
lst = s.split('_')
lst[0] = lst[0].title()
lst[1] = lst[1].title()
lst[2] = lst[2].title()
print("".join(lst))



s = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = s.split("*")
name = lst[0]
birthday = lst[1]
finish_date = lst[2]
birthday_year = birthday.split('-')[0]
finish_year =  finish_date.split('-')[0]
age = int(finish_year) - int(birthday_year)
data = name, age
print(data)







