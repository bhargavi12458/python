def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    n=int(input("enter any number:"))
    print('factorial value of',n,'is:',factorial(n))
    
