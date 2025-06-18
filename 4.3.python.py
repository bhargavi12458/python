def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    for i in range(1,11):
        result=factorial(i)
        print("factorial of",i,"is",result)
        
