#!/usr/local/bin/python3
# Convert stf transmittal in a Json file
# Revision 2016-12-12
# Copyright (c) 2016 Jeremy Heyl and Elisa Antolini


#from subprocess import call
import json
import re
import sys
import subprocess
import cStringIO





def CleanString(content):

    x = ''
    y = ''

    for j in content:

        if j == ":":
            line  = content
            Indexline = line.index(":")-1


            if line[Indexline] != "[" :
                x = content.rsplit(':', 1)[0] ## Will contain the strings before ':' character
                x = x.strip('\n')
                x = x.strip(' ')
                x = x.replace("->","__")

                y = line[line.find(':')+1 :  ] ## Will contain the strings after ':' character
                y = y.strip('\n')
                y = y.strip(' ')

    return(x,y)

'''
def jparseFile(line,i,EndValue):
    currentlevel=-1
    dict={}
    p = re.compile('^\s*-')
    newline  = []

 
    
    while i< EndValue:
 
            #print(line[i])
            
            if (len(line)==0):
               return dict
            
            if p.match(line[i])!= None:
                minuspos=line[i].index('-')
                
                
                if (currentlevel==-1):
                    currentlevel=minuspos
                    print(str(currentlevel)+" "+str(line[i])+" "+str(i))
                    print("\n")
                    i = i+1
                
            
                else:
                    if (currentlevel<minuspos):
              
                        print("i = "+str(i)+"-"+str(len(line)))
                        newline  = line[i:len(line)]
                        EndValue = len(newline)
                        #print(EndValue)
                        
                        newdict=jparseFile(newline,0,EndValue)
                        #print(newdict)
                        
                    
                        line[i].strip()
                        line[i] = line[i].strip(' ')
                        line[i] = line[i].strip('-')
                        line[i] = line[i].strip(' ')
                        line[i] = line[i].strip('\n')
                    
                        dict[line[i]]=newdict
                        #print(dict)
                        #print("\n")
                        i = i+1
                
       
                    else:
                       
                       #print("Currlevel = " +str(currentlevel))
                       #print("Minuspos  = " +str(minuspos))
                       #print(str(line[i])+" "+str(EndValue))
                       #print(k)
                        print("i = "+str(i)+"-"+str(len(line)))
                        line  = newline[i:len(line)]
                        EndValue = len(line)
                        #print(dict)
                        #i = 0
                        #i = i+1
                        return dict
            else:
                key,content = CleanString(line[i])
                dict[key]=content
                #print(dict)
                #print(str(line[i])+" "+str(i))
                i = i+1
       
                    
       
           
    
    return dict

'''

def jparseFile(f):
    currentlevel=-1
    dict={}
    p = re.compile('^\s*-')

    while True:
        line=f.readline()
        
        
        if (len(line)==0):
            return dict
        if p.match(line)!= None:
            minuspos=line.index('-')
            
            if (currentlevel==-1):
                currentlevel=minuspos
            #print(str(currentlevel)+" "+str(line))
            
            else:
                if (currentlevel<minuspos):
                    

                    f.seek(-len(line),1)
                    newdict=jparseFile(f)
               
                    #print(newdict)
                    #print("\n")
                    
                    line.strip()
                    line = line.strip(' ')
                    line = line.strip('-')
                    line = line.strip(' ')
                    line = line.strip('\n')
                    
                    dict[line]=newdict
                    #print(dict)
                else:
                    f.seek(-len(line),1)
                    #print(dict)
                    return dict
        else:
            key,content = CleanString(line)
            dict[key]=content
            #print(dict)
    
    return dict


#------------------------------------------------------------------------------
# main
#
def main():
    """
    This is the main routine.
    """


filename = sys.argv[1]


cmd = ['depth','-v',filename]

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)


Dictionary = jparseFile(cStringIO.StringIO(proc.stdout))



'''
StfOut = proc.stdout.read()
StfOut = StfOut.decode("utf-8")
StfOut = StfOut.split("\n")

line = []



for i in range(7,len(StfOut)-14):
    line.append(StfOut[i])



fname = open('DepthOutTrial.csv','r')

line = fname.readlines()

Dictionary = jparseFile(line,0,len(line))

#Dictionary = jparseFile(fname)

#print(Dictionary)
'''

with open('STFDepthOutProva2.json', 'w') as outfile:
     json.dump(Dictionary, outfile, indent = 2)

#------------------------------------------------------------------------------
# Start program execution.
#
if __name__ == '__main__':
    main()

