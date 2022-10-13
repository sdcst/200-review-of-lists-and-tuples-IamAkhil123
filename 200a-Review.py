#!python3

def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = []
    for i in myList:
         x = isinstance(i,int)
         if x == True:
             integers.append(i)
    return integers

def getFactor(myList, factor):
    # myList : expected list or tuple
    # factor : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
    for i in myList:
        x = factor / i
        p = int(x)
        if p == x:
            factors.append(i)
    return factors
    
def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
  negatives = []
  for i in myList:
      if i < 0:
          negatives.append =(i)
  return negatives

def getIntersection(list1,list2):
  common = []
  for i in list1:
      for t in list2:
          if i ==t:
              common.append(i)

  return common

def getUnion(list1,list2):

    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in either of the lists
    # the union of the 2 number sets
    union = []
    union = list1 + list2
    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
 merge = []
 for x in list2:
  list1.append(x)
 myList = list(dict.fromkeys(list1))
 return myList

def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    list1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    list2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    print(getIntegers(easy1))
if __name__ == "__main__":
    main()