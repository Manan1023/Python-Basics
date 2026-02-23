d1={'1':{"263":100000,"225":10000,"210":200000},
    '2':{"263":100000,"225":10000,"210":200000},
    '3':{"263":100000,"225":10000,"210":200000},}
for k,v in d1.items():
    print("Maximum and Minimum values in department ",k)
    ls=[]
    for l,m in v.items():
        ls.append(m)
    for l,m in v.items():
        if m==max(ls):
            print("Roll no. of maximum = ",l,"Salary = ",max(ls))
        if m==min(ls):
            print("Roll no. of minimum = ",l,"Salary = ",min(ls))
    