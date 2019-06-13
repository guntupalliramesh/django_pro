import datetime
from zipfile import ZipFile

ZipPath = input("\nEnter The Path Of The ZIP File :")

with ZipFile(ZipPath,'r') as zFile:
    for zInfo in zFile.infolist():
        print("\nName Of The ZIP File :",zInfo.filename)
        print("\nCREATED TIME :",datetime.datetime(*zInfo.date_time))
        print("\nCompressed Size :",zInfo.compress_size,"bytes")
        print("\nActual Size :",zInfo.file_size,"bytes")


