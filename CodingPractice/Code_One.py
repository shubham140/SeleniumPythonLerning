def is_curzon(num):
    a=(2 **num)+1
    b=(2*num)+1
    if(a%b==0):
        return True
    else:
        return  False


print(is_curzon(5))