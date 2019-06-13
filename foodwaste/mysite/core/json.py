# import json
#
# x = {
#   "name": "Ken",
#   "age": 45,
#   "married": True,
#   "children": ("Alice","Bob"),
#   "pets": ['Dog'],
#   "cars": [
#     {"model": "Audi A1", "mpg": 15.1},
#     {"model": "Zeep Compass", "mpg": 18.1}
#   ]
# }
# # sorting result in asscending order by keys:
# sorted_string = json.dumps(x, indent=4, sort_keys=True)
# print(sorted_string)



# import json  # json library imported
# # json data string
# person_data = '{  "person":  { "name":  "Kenn",  "sex":  "male",  "age":  28}}'
# # Decoding or converting JSON format in dictionary using loads()
# dict_obj = json.loads(person_data)
# print(dict_obj)
# # check type of dict_obj
# print("Type of dict_obj", type(dict_obj))
# # get human object details
# print("Person......",  dict_obj.get('person'))


#
# import json
# #File I/O Open function for read data from JSON File
# data = {} #Define Empty Dictionary Object
# try:
#         with open('myjson.json') as file_object:
#                 data = json.load(file_object)
# except ValueError:
#      print("Bad JSON file format,  Change JSON File")

