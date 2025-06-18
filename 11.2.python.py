d={'apple':5,'banana':10,'orange':8}
for k in d:
    print(k)
    for v in d.values():
        print(v)
        for k,v in d.items():
            print(k,"--->",k)
            
