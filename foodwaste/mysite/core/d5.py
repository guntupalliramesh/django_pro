# import numpy
# import pandas
#
# dfvalues = {"NAMES":['Abhi','John','Maddy','Angel','Merry'],"AGE":['25','32','22','29','34']}
#
# dataFrame = pandas.DataFrame(dfvalues)
#
# print("\nGIVEN DATA FRAME\n",dataFrame)
#
# names_sortDataframe = dataFrame.sort_values(by='NAMES',ascending=1)
# print("\nSORTED ROWS BY NAMES COLUMN IN THE ASCENDING ORDER\n",names_sortDataframe)
#
# age_sortDataFrame = dataFrame.sort_values(by='AGE',ascending=0)
# print('\nSORTED ROWS BY AGE COLUMN IN THE DESCENDING ORDER\n',age_sortDataFrame)
#
# missingDFvalues = {'NAMES':['Abhi','John','Maddy','Angel','Merry','John'],'AGE':['25',numpy.nan,'22','29',numpy.nan,'42']}
# missingDataFrame = pandas.DataFrame(missingDFvalues)
# print('\nGIVEN DATA FRAME\n ',missingDataFrame)
#
# missingSortedDataFrame = missingDataFrame.sort_values(by='AGE',na_position='first')
# print('\nSORTED ROWS BY AGE COLUMN WITH MISSING VALUES FIRST\n:',missingSortedDataFrame)
