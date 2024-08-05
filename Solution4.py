def check_num(list):
    if list[0] == list[-1]:
        return True
    else :
        return False

verify = check_num([1,2,3,4,5])
print((verify))
verify = check_num([1,2,3,4,1])
print((verify))

#output
True
False
