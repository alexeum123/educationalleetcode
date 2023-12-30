class myClass:                      #Class creation, self required param for every function

    def __init__(self, nums):       #Constructor, nums additional parameter
        self.nums = nums            #Create member variable nums
        self.size = len(nums)       #Create member variable size

    def getLength(self):            #Access method to member variable size
        return self.size
    
    #call member function
    def getDoubleLength(self):      #Call member function getLength within member function
        return 2 * self.getLength()
    
obj = myClass([1,2,3])              #Create object of class
print(obj.getLength()   )                  #Call member function from object: 3