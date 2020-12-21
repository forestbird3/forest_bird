y=2020
if y%100==0:
    if y%400==0:
        year='leap'
    else:
        year='common'
elif y%4==0:
    year='leap'
else:
    year='common'

print(year)