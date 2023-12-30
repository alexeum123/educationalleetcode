# Leetcode Python Guide    :    Created by Alex Eum

#Individuals--------------------------------------------------------------------------------------------
n, m = 0, "abc"     #Multiple assignment
a, b, c = [1, 2, 3] #Unpacking, variables to array, number must equal length
n = None            #None instead of null

if n>2: ...     #if statement
elif n==2: ...
else: ...

#Loops--------------------------------------------------------------------------------------------------
while n<5: ... #while

for i in range(5):...         #for loop, 0 to 4    (last exclusive)
for i in range(2,6):...       #for loop, 2 to 5    (last exclusive)
for i in range(5, 1, -1):...  #decreasing for loop, 5 to 2

#Math---------------------------------------------------------------------------------------------------
n = n + 1;   n += 1 #Increment, no n++

print(5/2)       # /  is decimal division, returns 2.5
print(5//2)      # // is integer division, returns 2, rounds down (even negative),  2.5 -> 2
print(-3//2)     # // is integer division, return -2, rounds down (even negative), -1.5 -> 2
print(int(-3/2)) # / decimal division, cast to int, returns -1 correctly

print(10 % 3)            #modulo remainder, returns 1
print(-10 % 3)           #modulo remainder, returns 2 wrong (negative round down decimal division)
import math              #import math helpers
print(math.fmod(-10, 3)) #returns -1 correctly

print(math.floor(3/2)) #down to nearest int
print(math.ceil(3/2))  #up   to nearest int
print(math.sqrt(2))    #sqrt to decimal
print(math.pow(2,3))   #exp  to decimal

float("inf")  #default max value
float("-inf") #default min value
print(math.pow(2, 200) < float("inf")) #True, 2^200 less than infinity

#Arrays--------------------------------------------------------------------------------------------------
arr = [1, 2, 3, 4, 5]  #Initialize defined
print(arr)             #[1, 2, 3, 4, 5]
print(len(arr))        #Returns 3

size = 5               #Define length
nums = [1] * size      #Initialize repetitive: [1, 1, 1, 1, 1]

arr = [i for i in range(5)]       #List Comprehension, gets i: [0,1,2,3,4]
arr = [i+i for i in range(5)]     #List comprehension, gets i+i: [0,2,4,6,8]

arr = [ [0]*4 for i in range(4) ] #2D List: makes 4x4 list of 0's (index 0 to 3, each as list of 4 zeros)

arr.append(4)     #Python arrays dynamic, like stack
arr.append(5)     #Adds to end,        O(1) constant
arr.pop()         #Removes from end,   O(1) constant
arr.insert(1, 7)  #Insert at index,    O(n) linear
arr[0] = 0        #Index/Change value, O(1) constant
print(arr[-1])    #Access last value (if doesn't exist, error)
print(arr[-2])    #Access 2nd to last value (if doesn't exist, error) 

nums.reverse()                 #Reverses array,      O(n) linear
arr.sort()                     #Sort array ascending (increasing or alphabetical)
brr = sorted(arr)              #Store sorted array ascending in new variable
arr.sort(reverse=True)         #Sort array descending
arr.sort(key=lambda x: len(x)) #Lambda sort, key = length, ascending

print(arr[1:3]) #Slicing/Sublist, array[start:end] (end exclusive): [2, 3]
print(arr[0:4]) #Slicing/Sublist, array[start:end] (end exclusive): [1, 2, 3, 4]

for n in nums:...                                 #Array Loop, n is value
for n in reversed(nums):...                       #Array loop, n is value
for i in range(len(nums)):...                     #Array Loop, i is index, nums[i] is value
for i, n in enumerate(nums):...                   #Array Loop, i is index, n is value
for i, num in reversed(list(enumerate(nums))):... #Array Loop: reverse ( list ( enumerate (nums
for n1, n2 in zip(arr, nums):...                  #Zip gets same index element of 2 arrays simultaneously

#String Logic--------------------------------------------------------------------------------------------
s = "abc"; s = 'abc'

s[0] = "A"     #Strings immutable, error
s += "def"     #Update/Create new string, O(n) linear: 'abcdef'
print(s[0:2])  #String slicing: index 0 to 1 (end exclusive)

print(int("123") + int("123"))    #String to Int, addition
print(str(123) + str(123))        #Int to String, concatenation
print(ord("a")); print(ord("b"))  #ASCII Value of char: 97, 98

strings = ["ab", "cd", "ef"]
print("".join(strings)) #String Combine with "" delimitor: "abcdef"

#Queues (deques)-----------------------------------------------------------------------------------------
from collections import deque
queue = deque()      #Creation

queue.append(2)      #Append right,       O(1) constant
queue.appendleft(1)  #Append left,        O(1) constant
print(queue)         #Print: deque([1,2])
queue.pop()          #Pop right,          O(1) constant
queue.popleft()      #Pop left,           O(1) constant

#Hashset (No Duplicate)----------------------------------------------------------------------------------
mySet = set()                   #Creation
mySet2 = {i for i in range (5)} #Set comprehension, manual definition: {0, 1, 2, 3, 4}
mySet3 = set([1,2,3,1,2])       #List to set, removes duplicates: {1, 2, 3}

mySet.add(1); mySet.add(2)      #Adding,    O(1) constant
mySet.remove(2)                 #Remove.    O(1) constant
print(mySet)                    #Print: {1, 2}
print(len(mySet))               #Length: 2

print(1 in mySet)               #Existence search, True  O(1) constant
print(2 in mySet)               #Existence search, False O(1) constant

#Hashmap (No Duplicate Key)------------------------------------------------------------------------------
myMap0 = {}                           #Empty Creation
myMap = {'alice': 88, 'bob': 77}      #Defined Creation
myMap1 = { i: i*2 for i in range (3)} #Map comprehension: {0: 0, 1: 2, 2: 4}

myMap["jack"] = 90                    #Inserts map[key]=value pairs,           O(1) constant
myMap["bob"] = 77                     #Updates map[key]=value pairs (exists),  O(1) constant
myMap.pop("Alice")                    #Pop key, must exist or error,           O(1) constant
print("alice" in myMap)               #Existence search: True                  O(1) constant
print(len(myMap))                     #Number of keys: 2

for i in myMap:...                    #Loop through map, i as key,   myMap[i] as value
for val in myMap.values():...         #Loop through map,             val as value     from map.values()
for key, val in myMap.items():...     #Loop through map, key as key, val as value     from map.items()

#Tuple (Immutable Array)---------------------------------------------------------------------------------
tup = (1, 2, 3)                  #Creation
print(tup)                       #(1, 2, 3)
print(tup[0]); print(tup[-1])    #Can index, can't modify: 0, 3

myMap = {(1,2): 3}               #Tuple as key for hashmap, (1,2) is a key
print(myMap[(1,2)])              #Get value: 3

mySet = set(); mySet.add((1,2))  #Tuple as key for hashset, (1,2) is an element
print((1,2) in mySet)            #Existence search: True

#Heaps (Min/Max)-----------------------------------------------------------------------------------------
import heapq
minHeap = [] #Creation, minHeap by default (min at index 0) (not sorted)
heapq.heappush(minHeap, 3);heapq.heappush(minHeap, 1)    #Adds 3 and 1 to minHeap,   stores as [1, 3]
print(minHeap[0])                                        #Returns min: 1
while len(minHeap): print(heapq.heappop(minHeap))        #Pop values, comes out smallest to largest

maxHeap = [] #Creation, maxHeap by negating pushed values, un-negate popped values
heapq.heappush(maxHeap, -3); heapq.heappush(maxHeap, -1) #Adds -3 and -1 to maxHeap, stores as [-3, 1]
print(-1 * maxHeap[0])                                   #Returns max: 3
while len(minHeap): print(-1 * heapq.heappop(minHeap))   #Pop values, comes out largest to smallest

heapq.heapify([2, 1, 8, 4, 5])                           #Build heap from array in O(n) linear
while arr: print(heapq.heappop(arr))                     #Pop values, comes out largest to smallest

#Functions-----------------------------------------------------------------------------------------------
def myFunct(n, m): return n*m   #Function definition
print(myFunct(3,4))             #Function execution

def outer(a, b):                  #Outer Function
    c = "c" 
    def inner(): return a + b + c #Nested Function, has access to outer variable c
        
def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2 #Modifies original array original array
        nonlocal val    #Since val defined outside of scope (not in double), must set nonlocal to access
        val *=2
    helper()
    print(arr, val)
    
nums = [1,2]; val = 3; double(nums, val) #Successfully modified array and val: [2,4] 6

#Class----------------------------------------------------------------------------------------------------
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
print(obj.getLength())              #Call member function from object: 3
#---------------------------------------------------------------------------------------------------------

    