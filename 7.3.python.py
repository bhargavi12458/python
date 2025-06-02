def pal(s):
    s=s.lower()
    if len(s)<=1:
        return true
    elif s[0]!=s[-1]:
        return false
    else:
        return pal(s[1:-1])
    my input=input("enter a string:")
    if pal(my input):
        print(f"'{my input}'is a palindrome.")
        else:
            print(f"'{my input}'is not a palindrome.")
            
