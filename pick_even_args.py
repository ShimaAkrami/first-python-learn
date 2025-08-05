def is_even(n):
    return n%2==0
     
    

def pick_even (*args):
    res=[]
    for i in args:
        if is_even(i):
            res.append(i)
    return res

numbers=[int(x) for x in input().split() ]

print(pick_even(*numbers))
   
