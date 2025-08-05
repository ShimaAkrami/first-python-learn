def skyline(*args):
    res=0
    for i in args:
        if i >= res:
            res=i
    return res
        
numbers=[int(x) for x in input().split()]
print (skyline(*numbers))