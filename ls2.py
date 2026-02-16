import random 
odd_lst =[]
even_lst = []
for i in range (5):
    odd_lst.append(random.randrange(1,99,2))
for i in range (5):
    even_lst.append(random.randrange(2,100,2))
print("odd list : ",odd_lst)
print("even list : ",even_lst)

odd_lst[2] = even_lst

print("Modified list : ",odd_lst)

flat_lst = []

for i in range(len(odd_lst)):
    if (isinstance(odd_lst[i],list)):
        for j in range(len(odd_lst[i])):
            flat_lst.append(odd_lst[i][j])
    else :
        flat_lst.append(odd_lst[i])

print("Flattened list is : ",flat_lst)
flat_lst.sort()
print("The sorted list is : ",flat_lst)