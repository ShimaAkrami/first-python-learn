def sum_number(*args):
    res=0
    for i in args:
        res+=i

    return res
    


user_input=input()
number=[int(x) for x in user_input.split()]
result= sum_number(*number) 
print(result)
