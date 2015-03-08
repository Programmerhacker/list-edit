to_do = []
import time
exit=0
while (exit==0):
    input = raw_input("cmd>>")
    lst = input.split()
    if (lst[0]=="add"):
        if (lst[1] in to_do):
            print "Item ", (lst[1]), " alredy exists"
        else:
            to_do.append(lst[1])
            print "Successfuly added 1 item"
    elif (lst[0]=="delete"):
        if (len(lst)==1):
            ask = raw_input("Are you sure (y/n)")
            if (ask=="y"):
                length = len(to_do)
                to_do=[]
                print "Successfuly deleted ", length, " item(s)"
        elif (lst[1] not in to_do):
            print "Item ", (lst[1]), " does not exist"
        else:
            to_do.remove(lst[1])
            print "Successfuly deleted 1 item"
    elif (lst[0]=="list"):
        if (len(to_do)==0):
            print "to_do list is empty"
        else:
            print (to_do)
    elif (lst[0]=="exit"):
        exit=1
    elif (lst[0]=="help"):
        print "add [item to add]"
        print "adds the item after the space"
        print "delete [item to delete]"
        print "deletes the item after the space"
        print "delete with no space deletes all"
        print "(it asks before done)"
        print "list"
        print "lists all items (ignore the ['' ''])"
        print "That's just how Python formats it"
        print "credits"
        print "Display credits"
        print "help"
        print "Display help"
    elif (lst[0]=="credits"):
        print "copyright ® 2015"
        time.sleep(0.5)
        print "softwarematic inc all rights reserved"
        time.sleep(0.5)
        print "Thanks to python"
        time.sleep(0.5)
        print "And thanks a lot to Breakout Mentors"
    else:
        print "Unknown command try help for a list of comands"
