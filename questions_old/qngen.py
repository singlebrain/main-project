import csv
import numpy
i=0
for i in range(10):
    #name='questions/'+chr(i) +'h'
    with open("%02dh.csv"%i, 'wb') as csv:
        columnTitleRow = "qn, opt1, opt2, opt3, opt4, anw\n"
        csv.write(columnTitleRow)
        #for key in dic.keys():
        row = "what is qwe in %02x hard , ad,zxc,yhn,okm,zxc\n"%i
        csv.write(row)
    with open("%02dm.csv"%i, 'wb') as csv:
        columnTitleRow = "qn, opt1, opt2, opt3, opt4, anw\n"
        csv.write(columnTitleRow)
        #for key in dic.keys():
        row = "what is qwe in %02x medium , ad,zxc,yhn,okm,zxc\n"%i
        csv.write(row)
    with open("%02de.csv"%i, 'wb') as csv:
        columnTitleRow = "qn, opt1, opt2, opt3, opt4, anw\n"
        csv.write(columnTitleRow)
        #for key in dic.keys():
        row = "what is qwe in %02x easy, ad,zxc,yhn,okm,zxc\n"%i
        csv.write(row)