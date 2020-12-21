m,n,a,b,c,d=map(int,input().split())
fee=[a, b, d]
number=[1, 1, c]
money=m
animals=n
money=money-sum(fee)
animals=animals-sum(number)

#drivercode
for n_cows in range(0, animals+1):
    for n_sheeps in range(0, animals+1-n_cows):
        copy_of_animals = animals
        copy_of_animals -= n_cows + n_sheeps

        n_goat_packs = copy_of_animals / number[2]

        if n_goat_packs != int(n_goat_packs):
            continue

        copy_of_money = money
        copy_of_money -= fee[0] * n_cows
        copy_of_money -= fee[1] * n_sheeps
        copy_of_money -= fee[2] * n_goat_packs

        if copy_of_money== 0:
            print(n_cows+1, n_sheeps+1, int((n_goat_packs+1) * number[2]))
