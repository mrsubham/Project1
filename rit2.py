#forlogging
import os
import logging as log
import csv
fob1=open("configtemp.ini","r")

#log.debug("hello 1")
#log.info ("hello 2")
#log.warning("hello 3")
#log.error("hello 4")
#log.critical("hello 5")

log.basicConfig(level=log.DEBUG,filename="app.log")

dct={}
log.info("Collecting the values from config")
for line in fob1:
    if(line[0]=='[' and line[-2]==']'):
        pass
    else:
        line1=line
        p=line1.rstrip('\n')
        lst1=p.split('=')
        dct[lst1[0]]=lst1[1]
req_files=[]
log.info("Collecting the header files from the given path")
path=dct["inputfile"][1:-1]
flst=list(os.walk(path))
if(len(flst)==0):
    log.error("There are no header files in the specified path")


log.info("Writing the contents to csv file")


dct_write={"Date":"239193","Filename":"1.txt","Structname":"cacjnka","size":5}
dct_write2={"Date":"23ds9193","Filename":"2.txt","Structname":"sascacjnka","size":15}

lst_final=[dct_write,dct_write2]

lst_write=[]
flag=0
for finalele in lst_final:
    lst_write=[]
    dct_write=finalele
    for ele in dct_write:
        lst_write.append(dct_write[ele])
    with open('people.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        if(flag==0):
            writer.writerows([["Date","Filename","Structname","size"]])
            flag=1
        writer.writerows([lst_write])   
