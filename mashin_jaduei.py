n=int(input())
if 2<=n<=1000:
    while not n==1:
        if n % 2 == 0:
            n=n//2
         
        else:
            n=(n*3)+1
        print(n)

        
