#coding='utf-8'

def fun1():
    j=0
    for i in range(0,102,2):
        j=j+i
    return j

def fun2():
    a= 2+100
    return a*50/2

def fun3():
    i=100
    j=0
    while i>=2:
        j=j+i
        i=i-2
    return j


print (fun1())
print (fun2())
print (fun3())