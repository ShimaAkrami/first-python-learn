def sum_number(*args):
    res=0
    for i in args:
        res+=i

    return res
    if args==0:
        res=0
        return res


user_input=input()
number=[int(x) for x in user_input.split()]
result= sum_number(*number) 
print(result)
