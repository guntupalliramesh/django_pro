import numpy as np

givenArray = np.array([[1,3,6],
                       [2,10,9],
                       [12,4,8]])
sortedArray = np.sort(givenArray,axis=None)
print("\nSORTED ARRAY: \n",sortedArray)

rowsortedArray = np.sort(givenArray,axis=1)
print("\nROW-WISE SORTED ARRAY : \n",rowsortedArray)

colsortedArray = np.sort(givenArray,axis=0)
print("\nCOLUMN-WISE SORTED ARRAY : \n", colsortedArray)

algoSortedArray = np.sort(givenArray,axis=1,kind='quicksort')
print("\nALGORITHM SORTED ARRAY :\n", algoSortedArray)

print("________________________")

dtypeNames = [('name','S10'),('age',int)]

arrayValues = [('Abhi',25),
               ('John',32),
               ('Maddy',22),
               ('Angel',29),
               ('Merry',34)]

structArray = np.array(arrayValues,dtypeNames)
print("\nStructured Array :\n",structArray)
namesSortedArray = np.sort(structArray, order='name')
print("\nArray Sorted BY NAMES :\n",namesSortedArray)

ageSortedArray = np.sort(structArray,order='age')
print("\nARRAY SORTED BY AGE : \n", ageSortedArray)
