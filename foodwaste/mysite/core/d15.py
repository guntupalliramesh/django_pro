import random
def ODDevenSort(array1,arraylength):
    sortedArray = 0
    while sortedArray == 0:
        sortedArray = 1
        for a in range(0,arraylength -1,2):
            if array1[a]>array1[a + 1]:
                array1[a],array1[a + 1] = array1[a+1],array1[a]
                sortedArray = 0

        for a in range(1,arraylength-1,2):
            if array1[a]>array1[a+1]:
                array1[a],array1[a+1] = array1[a+1],array1[a]
                sortedArray = 0

if __name__ == '__main__':
    randomArray = random.sample(range(-10,20),8)
    print("\nBefore Sorting :",end=" ")
    for i in range(len(randomArray)):
        print(randomArray[i],end=" ")
    ODDevenSort(randomArray,len(randomArray))
    print("\n\nSorted Array : ",end=" ")
    for i in range(len(randomArray)):
        print(randomArray[i],end=" ")