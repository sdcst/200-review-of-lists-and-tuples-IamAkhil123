#!python3

def getIntegers(mylist):
    easy2 = mylist
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    mylist.append(mylist)
 
    return mylist

def getFactor(myList):
    easy2 = myList
    # myList : expected list or tuple
    # factor : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    num = 0
    while num < len(myList):
       if myList[num] % 2 == 0:
        print(myList[num], end=" ")
        num += 1
    
def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
  negatives = [x for x in myList if x <= 0 ]
  return negatives

def getIntersection(list1,list2):
  
 print("The original list 1 is : " + str(list1))
 print("The original list 2 is : " + str(list2))
  

 res = len(set(list1) & set(list2)) / float(len(set(list1) | set(list2))) 
  
 return ("Percentage similarity among lists is : " + str(res))


def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a list of numbers that is in either of the lists
    # the union of the 2 number sets
    union = []

    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    merge = list.copy()

    return merge


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    list1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    list2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    print(getIntersection(list1,list2))
if __name__ == "__main__":
    main()