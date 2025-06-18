d={'apple':5,'banana':10,'orange':8,'mango':15}
kd=['apple','banana']
for k in kd:
    if k in d:
        del d[k]
        print(d)
        
