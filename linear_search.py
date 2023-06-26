pos = -1

def search(list,n):
    i =0
    while i<len(list):
        if list[i]==n:
            globals() ['pos'] = i
            return True
        i+=1
    return False

list = [1,2,3,4,5,6,7,8,9]
n = 9
if search(list,n):
    print("Found",pos)
else:
    print("Not Found")