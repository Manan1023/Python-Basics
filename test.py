def f_to_c () :
    f = [45,25,56,89,14]
    c = [] 
    for i in f :
        c.append((i - 32)*5/9:.2f)
    print(c)

f_to_c()