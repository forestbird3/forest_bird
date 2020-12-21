y=2019
if y%400==0:
    year='leap'
elif y%100==0:
    year='common'
elif y%4==0:
    year='leap'
else :
    year='common'
print(year)