def solutions(a, b, c):

    d=b*b-(4*a*c)
    if(d>0):
        return 2
    elif(d==0):
        return 1
    else:
        return 0


print(solutions(1,0,1))