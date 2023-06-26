class linear_search:
    def __init__(self,list,n):
        self.list = list
        self.n = n
        self.pos=-1
        self.done=1
    def search(self):
        done = 0
        for i in self.list:
            if self.list[i]==self.n:
                self.pos= i+1 
                self.done = 1
                break
        if self.done == 1:
            print("Found",self.pos) 
        else:
            print("Not Found")
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]   
n = int(input("Enter the number to be searched(1-50):"))
linear_search = linear_search(list,n)
linear_search.search()
