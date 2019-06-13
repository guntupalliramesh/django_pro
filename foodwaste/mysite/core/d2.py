def convertTime(iptime):
    if iptime[:2] == "12" and iptime[-2:] == "AM":
        convertTime = "00"+iptime[2:-2]
        return convertTime
    elif iptime[-2:] == "AM":
        return iptime[:-2]
    elif iptime[:2] == "12" and iptime[-2:] == "PM":
        return iptime[:-2]

    else:
        convertTime = str(int(iptime[:2]) + 12) + iptime[2:8]
        return convertTime

InputTime = input("\nEnter THE TIME :")
print("\nCONVERTED TIME :",convertTime(InputTime))