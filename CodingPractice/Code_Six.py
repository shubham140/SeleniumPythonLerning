def total_overs(balls):
    a=balls//6
    b=balls%6
    c=str(a)+"."+str(b)
    return c



a=total_overs(945)
print(a)