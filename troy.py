msg=['win','next']
troy,wood,ready=map(int,input().split())
r=0
if troy*wood>ready: r=1
print(msg[r])
