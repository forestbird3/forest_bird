def coffee(n,s=''):
    if n == 0:
        print(s)
        return
    for i in set(word):
        coffee(n-1,s+i)
    #coffee(n-1,s+'c')
    #coffee(n-1,s+'o')
    #coffee(n-1,s+'f')
    #coffee(n-1,s+'e')

#driver code
n=3
word='coffee'
a=set(word)
coffee(n)
        