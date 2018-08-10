#arch
#cellpad
#inputfile
#outputfile
#logfile
import glob
import os
fob1=open("config.ini","r")
dct={}
for line in fob1:
    if(line[0]=='[' and line[-2]==']'):
        pass
    else:
        line1=line
        p=line1.rstrip('\n')
        lst1=p.split('=')
        dct[lst1[0]]=lst1[1]

req_files=[]
path=dct["inputfile"][1:-1]
flst=os.walk(path)
for ele in flst:
    #print(type(ele))
    files=ele[-1]
    for ele1 in files:
        if ele1.endswith('.h'):
            req_files.append(path+"/"+ele1)

print(req_files)
    
