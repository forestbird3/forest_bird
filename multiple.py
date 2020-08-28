print("구구단을 몇단을 계산할까요?")
variable=input()
print("구구단 " + variable + "단을 계산합니다.")
int=int(variable)
for i in range(1,10):
    result = int * i
    print(variable, "X", i,"=", result)
