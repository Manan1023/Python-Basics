l1 = [("Manan",),("Nirav",),"Nirali","Bhakti","Dhruvi"]
b,g = 0,0
for e in l1:
    if isinstance(e,tuple):
        b+=1
    else:
        g+=1
print("Boys = ",b,"Girls = ",g)