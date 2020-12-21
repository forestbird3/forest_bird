income=int(input())
grade=['Bottom 10','Bottom 20','Bottom 50','Bottom 75','Bottom 85','Top 1','Top 5','Top 10','the middle']
if income<=400: a=0
elif income<=500: a=1
elif income<=850: a=2
elif income<=1487: a=3
elif income<=2182: a=4
elif income>=47500: a=5
elif income>=33700: a=6
elif income>=25400: a=7
else: a=8
print(grade[a])
