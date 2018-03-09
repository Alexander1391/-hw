day = '05.17.2016'
s = day.split(':')
s[:2],s[3:5],s[6:] = s[3:5], s[:2], s[6:]
print(''.join(s))

name = "Mark Zuckerberg"
adc = name.split()
adc[0], adc[1] = adc[1], adc[0]
print(" ".join(adc))

s = 'employee_first_name'
lst = s.split()
s1 = (s.title ()[:7])
s2 = (s.title ()[9:14])
s3 = (s.title()[15:])
s4 = s1 + s2 +s3
print(s4)


s = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = s.split()
name = format (s[:11])
born = int (s[12:16])
dead= int (s[23:27])
total_result = name , dead - born
print(total_result)












