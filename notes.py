# Leetcode Python Guide

#Multiple assignment
n, m = 0, "abc"

#increment, cannot do n++
n = n + 1
n += 1

#None replace null
n=4
n = None

#if statement
if n>2:
    n-=1
elif n==2:
    n-=2
else:
    n-=3

#while
while n<5:
    n+=5

#for loop (incremented automatically)
    #goes 0 to 4
    for i in range(5):
        print(i)

    #goes from 2 to 5, last number in range excluded
    for i in range(2,6):
        print(i)
    #decrement (must specify), goes from 5 to 2
    for i in range(5, 1, -1):
        print(i)


#division is decimal, will return 2.5
print(5/2)

#integer division (always rounds down, even negative)
print(5//2) #2, since 2.5 rounded down
print(-3//2) #-2, since -1.5 rounded down

#use standard decimal division, conver to int
print(int(-3/2)) #returns -1 correctly

#modulo, different when negative
print(10 % 3) #returns 1
print(-10 % 3) #returns 2

#import math helpers
import math
print(math.fmod(-10, 3)) #returns -1 correctly

print(math.floor(3/2)) #down to nearest int
print(math.ceil(3/2)) #up to nearest int
print(math.sqrt(2)) 
print(math.pow(2,3)) #like 2^3

#default max/min
float("inf") #max
float("-inf") #min
#python numbers are infinite, never overflow

print(math.pow(2, 200)) #less than infinity
print(math.pow(2, 200) < float("inf")) #true

#--------------------------------------------------------------------------------------------
#Arrays

arr = [1, 2, 3] 
print(arr)      #1, 2, 3
print(len(arr)) #returns 3

#Python arrays are dynamic by default, can be used like stacl
arr.append(4) #1, 2, 3, 4
arr.append(5) #1, 2, 3, 4, 5
arr.pop()     #1, 2, 3, 4

#Can insert into the middle, puts value at index
# O(n) operation
arr.insert(1, 7) #1, 7, 2, 3, 4

#Indexing is constant time, can assign
# O(1) operation
arr[0] = 0

#Initialize array of size n with default value of 1
size = 5
arr = [1] * size #1, 1, 1, 1, 1

#When indexing, -1 is last value, -2 second to last
#if not enough, will then index out of bounds
arr = [1, 2, 3] 
print(arr[-1]) #prints 3
print(arr[-2]) #prints 2

#Slicing & Sublists
arr = [1,2,3,4]
#prints index 1 to 3, not including last
print(arr[1:3]) # returns 2, 3
print(arr[0:4]) #returns 1, 2, 3, 4

#unpacking, variable to array assignment
#must make sure number of variables on left matches length of array
a, b, c = [1, 2, 3]
nums = [1, 2, 3]

#loop through array with index via range(len)
for i in range(len(nums)):
    print(nums[i]) #we have index

#loop through array with actual value
for n in nums:
    print(n) #we have value

#loop through array with index and value
for i, n in enumerate(nums):
    print(i, n) #i is index, n is value

#for loop values in a reversed list
for num in reversed(nums):
    print(num)

#enumerate on its own is not reversiblee
#must turn enumerate into a list
for i, num in reversed(list(enumerate(nums))):
    print(i, num)


#loop through multiple arrays simultaneously with zip
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    #1 2
    #3 4
    #5 6

#reverse array
nums = [1, 2, 3]
nums.reverse()
print(nums) #[3, 2, 1]

#sorting numbers (ascending default)
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr) #3, 4, 5, 7, 8

#sort in descending (reverse order)
arr.sort(reverse=True)
print(arr) #8, 7, 5, 4, 3

#sorting string (alphabetical default)
arrName = ["bob", "alice", "jane", "doe"]
arr.sort() 
print(arr) #['alice', 'bob', 'doe', 'jane]

#custom sorting of string array with lambdas
#take each value in array, treat it (key) as its length,
#sort by the key
#so this will sort by increasing length of string
#string mapped to its length
arr.sort(key=lambda x: len(x))

#list comprehension
#add default 0 to 4 into array
arr = [i for i in range(5)]
print(arr) # [0,1,2,3,4]

#modify numbers before adding to array
arr = [i+i for i in range(5)]
print(arr) #0, 2, 4, 6, 8

#------------------------------------------------------------------------------
#2D Lists

#makes 4 lists (indexed 0,1,2,3) each with 4 zero's (rows unique)
#4x4 list
arr = [ [0]*4 for i in range(4)]

#------------------------------------------------------------------------------
#String Logic

s = "abc"
s = 'abc'

#Strings are immutable
s[0] = "A" #will not work

#Can 'update' or create new string
# O(n) time operation
s += "def"
print(s) #abcdef

#string slicing
print(s[0:2]) #gets from index 0 to 1 (last index exclusive)


#String Integer conversions valid both ways
print(int("123") + int("123")) #246, addition
print(str(123) + str(123)) #123123, concatenation

#ASCII value of a char
print(ord("a")) #97
print(ord("b")) #98

#combine list of strings (with empty string delimitor)
#delimitor is what goes in between combined strings
#usually empty "" or comma ","
strings = ["ab", "cd", "ef"]
print("".join(strings)) #abcdef


#------------------------------------------------------------------------------
#Queues (double ended deques by default)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)

print(queue) #deque([1,2])

#left pop constant time operation, O(1)
queue.popleft()
print(queue) #deque([2])

#can add to the left
queue.appendleft(1)
print(queue) #deque([1,2])

#right pop 
queue.pop()
print(queue) #deque([1])


#------------------------------------------------------------------------------
#Hashset, does not allow duplicate
#search and insert and remove in constant time O(1)

mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet) #{1, 2}
print(len(mySet)) #2

#search with 'in' operator
print(1 in mySet) #True
print(3 in mySet) #False

#remove
mySet.remove(2)
print(2 in mySet) #False

#list to set
print(set([1,2,3]))

#set comprehension, manually initialize
mySet = {i for i in range (5)} #0, 1, 2, 3 4

#------------------------------------------------------------------------------
#Hashmap
#cannot have duplicate keys

#empty
myMap = {}

#initialize with value
myMap = {'alice': 88, 'bob': 77}

#insert with key to value
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap) #{'alice': 88, 'bob': 77}

#len is number of keys
print(len(myMap)) #2

#modify value mapped to a key
myMap["alice"] = 88

#search if a key exists, constant time
print("alice" in myMap) #True

#remove key in constant O(1) time, must exist or error (check first)
myMap.pop("Alice")

#dict comprehension
myMap = { i: i*2 for i in range (3)} #{0: 0, 1: 2, 2: 4}


#looping through map with key
for key in myMap:
    print(key, myMap[key])

#loop through map with direct values via .values() (if we dont need key)
for val in myMap.values():
    print(val)

#loop through key and values via .items()
for key, val in myMap.items():
    print(key, val)

#------------------------------------------------------------------------------
#Tuples
#arrays but immutable

tup = (1, 2, 3)
print(tup) #1, 2, 3

#can index
print(tup[0])
print(tup[-1])
#can't modify

#use tuples as key for hashmap
#map a pair of values (1,2) to 3
myMap = { (1,2): 3}
print(myMap[(1,2)]) #3

#use tuples as key for hashset
mySet = set()
mySet.add((1,2))
print((1,2) in mySet) #True

#lists cannot be keys due to their mutability
#tuples are good for keys because they can't be changed


#------------------------------------------------------------------------------
#Heaps
#find min and max, implemented as ararys in python
import heapq

#by default, heaps in pythons are minHeaps
#so min is always at index 0, heap not necessarily sorted though
minHeap = []
heapq.heappush(minHeap, 3) #add 3 to that minHeap
heapq.heappush(minHeap, 2) #add 2 to that minHeap
heapq.heappush(minHeap, 1) #add 1 to that minHeap
print(minHeap[0]) #returns 1, the min

#pop values, will come out smallest to largest
#since smallest always at index 0
while len(minHeap): 
    print(heapq.heappop(minHeap))


#no max heap, but just multiply each value by -1 while pushing
#and multiply by -1 when popping
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

#Max always at index 0
#multiply by -1 to revert/undo initial -1 multiplication
print(-1 * maxHeap[0])

while len(minHeap): 
    print(-1 * heapq.heappop(minHeap))

#build heap in linear time from values with heapify
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr) #turn into heap

while arr:
    print(heapq.heappop(arr)) #will print values smallest to largest


#------------------------------------------------------------------------------
#Functions
    
def myFunct(n, m):
    return n*m

print(myFunct(3,4))

#nested functions
#inner functions have access to outer variables
def outer(a, b):
    c = "c"
    def inner():
        return a + b + c

#can modify objects but not reassign unless using nonlocal keyword
def double(arr, val2):
    def helper():
        #modify array
        for i, n in enumerate(arr):
            arr[i] *2 #will modify original array
        
        #will only modify the val in helper scope
        val *= 2 #value is still original outside of helper

        #to update value everywhere (outside helper scope)
        #set as nonlocal
        nonlocal val2 
        val2 *=2
    
    helper()
    print(arr, val)

nums = [1,2]
val = 3
double(nums, val) #[2,4] 6
#successfully doubled both bc arrays modify regardless
#value modified using nonlocal keyword



#------------------------------------------------------------------------------
#Class

#self is passed into every method of a class, like this keyword
class myClass:
    #Constructor
    def __init__(self, nums): #nums we choose to pass in
        #create member variables
        self.nums = nums
        self.size = len(nums)

    #self key word required as parameter
    #access to member variable
    def getLength(self):
        return self.size
    
    #call member function
    def getDoubleLength(self):
        return 2 * self.getLength()
    

    
    
    































