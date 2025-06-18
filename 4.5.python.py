def calculate_sum(numbers):
    total=0
    for num in numbers:
        total+=num
        return total
    list=[]
    n=int(input("enter the number of elements in the list:"))
    for i in range(n):
        num=eval(input("enter the element{}:",format(i+1)))
        list.append(num)
        result=calculate_sum(list)
        print("the sum of the list is",result)
        
