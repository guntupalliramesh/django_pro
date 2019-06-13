import pandas
#
# dValues = {'NAMES':['Abhi','John','Maddy','Angel','Merry'],'AGE':['25','32','22','29','34']}
# dataFrame = pandas.DataFrame(dValues)
# print("\nGiven DATA Frame\n",dataFrame)
# print("\nIterating Over Rows Using Iterrows()\n")
# for i,j in dataFrame.iterrows():
#     print(i,j,"\n")
#
# print("\nIterating Over Rows Using Iteritems()\n")
# for i,j in dataFrame.iteritems():
#     print(i,j,"\n")
#
# print("\nIterating over rows using itertuples()\n")
# for i in dataFrame.itertuples():
#     print(i,"\n")
#
# print("\nPrinting the fourth element present in the dataframe\n")
#
# columns = list(dataFrame)
# for i in columns:
#     print(dataFrame[i][3])

import csv

df = pandas.read_csv("EQ060519.CSV")
ser = pandas.Series(df['SC_NAME'])
de= ser.head(10)
print(de[3:8])