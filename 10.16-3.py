a='123456789'
for i in range(9):
    s=a[:i+1]
    w='{0:>9s}*8+{1}={2}'.format(s,i+1,int(s)*8+i+1)
    print(w)

#a=0
#for i in range(1,10):
    #a=a*10+i
    #w='{0:10d}*{1}+{2}={3}'.format(a,8,i,a*8+i)
    #print(w)