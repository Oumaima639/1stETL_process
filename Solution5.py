def divided_num(list,target):
    list2 = []
    for i in list:
        if i%target == 0:
            list2.append(i)
    return list2

list = [1,2,3,4,5,10,15,2]
verif = divided_num(list,5)
print(verif)

#output
[5,10,15]
