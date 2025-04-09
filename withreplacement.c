>>> name="python"
>>> sal=60000
>>> gf="java"
>>> print("hello{}your friend{}is waiting and your sal is{}".format(name,sal,gf))
hellopythonyour friend60000is waiting and your sal isjava
>>> print("hello{0}your friend{1}is waiting and your sal is{2}".format(name,sal,gf))
hellopythonyour friend60000is waiting and your sal isjava
>>> print("hello{x}your friend{y}is waiting and your sal is{z}".format(z=gf,y=sal,x=name))
hellopythonyour friend60000is waiting and your sal isjava