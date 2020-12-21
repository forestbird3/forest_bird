msg=('leap','common')
y=2019
m=y%4!=0 or (y%100==0 and y%400!=0)

print(msg[m])