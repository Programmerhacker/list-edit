to_do = []
input = raw_input("cmd>>")
lst = input.split()
if (lst[0]="add"):
    to_do.append(lst[1])
elif (lst[0]="delete"):
    to_do.remove(lst)
elif (lst[0]="list"):
    print (to_do)
