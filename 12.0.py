from turtle import *
def tree(n,s,a,w):
    if n==0: 
        dot(200,'lightgreen')
        return
    x,y=position()
    setheading(a)
    width(w)
    fd(s)
    tree(n-1,s*0.7,a-45,w*0.7)
    tree(n-1,s*0.7,a+45,w*0.7)
    goto(x,y)

'''driver code'''
setup(800,800)
width(20)
pencolor('brown')
speed(100)
up(); goto(0,-300); down()
tree(8,200,90,30)
done()