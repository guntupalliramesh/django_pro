# import json
# import socket
# import getpass
# from  urllib.request import urlopen
#
# username = getpass.getuser()
# print("\nUSERNAME : ",username)
#
# hostname = socket.gethostname()
# print("\nHOSTNAME : ",hostname)
#
# machineIP = socket.gethostbyname(hostname)
# print("\nIP ADDRESS : ",machineIP)
#
# url = 'http://ipinfo.io/json'
# response = urlopen(url)
#
# data = json.load(response)
#
# print("\nPUBLIC IP : ",data['ip'])
# print("\nCITY : ",data['city'])
# print("\nSTATE : ",data['region'])
# print("\nCOUNTRY : ",data['country'])