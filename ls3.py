import random 
def random_numbers () :
    lst = []
    lst = [random.randint(1,50) for x in range (50)]
    print("Old list :",lst)
    new_lst = []
    for i in lst :
        if i not in new_lst:
            new_lst.append(i)
    print("New list :" , new_lst)

random_numbers()


