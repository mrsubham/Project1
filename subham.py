#arch
#cellpad
#inputfile
#outputfile
#logfile
import glob
import re
import os
fob1=open("config.ini","r")
dct={}
dct_32={"int":4,"char":1,"float":8,"*":4}
dct_64={"int":8,"char":1,"float":8,"*":8}
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


di={}
if dct["arch"] == "64":
    di=dct_64
else : di=dct_32
if dct["cellpad"] == "true":
    di["char"]=4
files=req_files
print(di)
file_struct=[]
for file in files:
    
    print("In File: ",file)
    fob=open(file,"r")
    openbrace_flag=0
    total_size=0
    struct_names={}
    for i in fob:
        i=i.rstrip()
        
        print("In line:",i,openbrace_flag)
        if i.split()[0]=="struct" or openbrace_flag==1 :
            print(i.split())
            
            for j in range(len(i.split())):
                if i.split()[j] == "int":
                    temp = i.split()[j+1].split(',')
                    count=0
                    for l in temp:
                        if l[0] == '*':
                           total_size=total_size+di["*"]
                           count=count+1
                        else :
                            total_size=total_size+di["int"]
##                    k=len(i.split()[j+1].split(','))
##                    total_size=total_size+di["int"]*(k-count)
##                    print("Calculating size of",i.split()[j],i.split()[j+1].split(','),k,di["int"]*k)
                elif i.split()[j] == "char":
                    k=len(i.split()[j+1].split(','))
                    total_size=total_size+di["char"]*k
                    print("Calculating size of",i.split()[j],i.split()[j+1].split(','),k,di["int"]*k)
                elif i.split()[j] == "float":
                    k=len(i.split()[j+1].split(','))
                    total_size=total_size+di["float"]*k

                    print("Calculating size of",i.split()[j],i.split()[j+1].split(','),k,di["int"]*k)
                elif i.split()[j] == "struct" and openbrace_flag == 1:
                    total_size=total_size+struct_names[i.split()[j+1][:-1]]
                else : print("skipping")
            
                
            
            if openbrace_flag == 0:
                struct_name=i.split()[1]
                if struct_name in struct_names:
                    total_size=total_size+struct_names[struct_name]
            if i.split()[-1] == '};':
                openbrace_flag=0
                struct_names[struct_name]=total_size
                total_size=0
                print("i am out of " ,struct_name)
                struct_name=""
                print(struct_names)
            if i.split()[-1] == '{' :
                openbrace_flag=1
                print("Flag open")
    file_struct.append(struct_names)
            
            
            
