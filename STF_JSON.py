#!/usr/local/bin/python3

import os
import sys
import shutil

from subprocess import call

from itertools import groupby
import json

import re
import numpy as np


### UNCOMMENT THIS FOR GENERATE THE CSV output file from the Transmittal ####
#call('depth -v LMBX_cat.stf > DepthOut.csv', shell=True)


### This is a csv file version shorter than the original one, just for made a trial ####

fname = 'DepthOutProva.csv'

x=[]

#### Read the csv file generated from Depth command #####


with open(fname) as f:
    content = f.readlines()



#def parseFile(filehandle,currentline):

    # Keep the track of where the braket is, if increases call the parseFile again
    # When the bracket comes again goes return
    # Build the dictionary
    # Read the previous line
    # Line which starts with - IS A NEW OBJECT -> Start to create a dictionary
    # wWhere is the - signs (columns)


def CleanString(content):

    x = ''
    y = ''

    for j in content:

        if j == ":":
            line  = content
            Indexline = line.index(":")-1


            if line[Indexline] != "[" :
                x = content.rsplit(':', 1)[0] ## Will contain the strings before ':' character

                y = line[line.find(':')+1 :  ] ## Will contain the strings after ':' character

    return(x,y)


#print(content[k])

def FindLevel(tree,index):
    dim = len(index)
    #print(dim)
    key = 'None'
    keyindex = 0
    count = dim -1

    
    if dim > 2:
        
        for j in range(1,dim):

            #Searching for the same tree level
            
            if index[count] == index[count-j] :
                key = tree[count-j]
                keyindex = count-j
                return(key,keyindex)
            else :
                key = 'None'
                keyindex = 0
    
        #Searching for a lower level
        
        if key == 'None' :
            a = index[0:count]
            
            maximum = max(a)
            maxind = a.index(maximum)
            #print(max(a),maxind)
            minimum = min(a)
            
            if index[count] > maximum :
                key = tree[maxind]
                keyindex = maxind
                return(key,keyindex)
   
    

        return(key,keyindex)

    if dim == 2 :
        
        key = tree[count-1]
        keyindex = count-1
        return(key,keyindex)

    if dim == 1 :
        return('None',0)


def parseFile(lastline,Indexline):

    currentline = 0
    treelevel = 0
    treecontent =''
    dict = {}

    #x=[]
    #y=[]

    #for k in range(len(content)) :
    for k, line in enumerate(content):

       p = re.compile('^\s*-')
       currentline = k+1

       if p.match(line)!= None and treelevel < 2:

          if  currentline >= lastline :
              treelevel   = treelevel +1
              #Indexline   = line.index("-")
              #print(Indexline,line)

              if   treelevel == 1:
                   treecontent = line
                   Indexline   = line.index("-")
                   #print(Indexline,line)
                  # Define the object in the Dictionary
                   dict[line] = {}



       if p.match(line)== None and treelevel < 2:

           #print(line)
           if  currentline > lastline :
                x,y = CleanString(line)
           #Define the content in the object Tree
                #print(treecontent)
                (dict[treecontent])[x] = y
           #print(currentline,x+"   "+ y+"\n")

                if  currentline == len(content) :
                    lastline = k+1
                    return(lastline, dict, Indexline, treecontent)


       if  treelevel == 2 :
           lastline = k+1

           print("\n")

           return(lastline, dict, Indexline, treecontent)



Dictionary={}
lastline  = 0
Start = 0
Index = 0
line = 0
TreeContent = []
IndexTree = []
count = 0
treecontent = ''
j = 0


maximum = 0

while (j < len(content)):



       lastline, dict, Index, treecontent = parseFile(lastline,Index)
       j = lastline

       IndexTree.append(Index)
       TreeContent.append(treecontent)
       #print(IndexTree[count],TreeContent[count])
       
       key, keyindex = FindLevel(TreeContent,IndexTree)
       #print(key,keyindex)
       print(dict)
       
       if key == 'None' :
           Dictionary = dict
       
       else:
           (Dictionary[TreeContent[0]])[key] = dict


       #print(Dictionary)
       count = count +1



### This is the data format for create a JSON file with the same tree structure of the STF file ####

# Dictionary

'''
dataDic ={content[0]:{x[0]:content[1],x[1]:content[2],x[2]:content[3],x[3]:content[4],x[4]:content[5],x[5]:content[6],x[6]:content[7],
x[7]:content[8],x[8]:content[9],x[9]:content[10],x[10]:content[11],x[11]:content[12],x[12]:content[13],content[14]:{content[15]:{x[13]:content[16], x[14]:content[17],x[15]:content[18],x[16]:content[19],x[17]:content[20],x[18]:content[21],x[19]:content[22],x[20]:content[23],x[21]:content[24],x[22]:content[25]},content[26]:{content[27]:{content[28]:{ x[23]:content[29],x[24]:content[30],x[25]:content[31]}}, content[32]:{x[26]:content[33]}, content[34]:{x[27]:content[35],x[28]:content[36],x[29]:content[37],x[30]:content[38] }  }}}}

### Generate the JSON file ###

with open('STFDepthOut.json', 'w') as outfile:
    json.dump(dataDic, outfile, indent=4)

'''

'''

names = ["transmittal","language","country"]


with open("DepthOutProva.csv") as f, open("STFDepthOutTrial.json","w") as out:

    data = map(str.rstrip,f)
    grouped = groupby(data, key=lambda x: x.startswith("-[:"))
    #gb = grouped.groups


    for k,v in grouped:
        print(v)
        #print(grouped.get_group(k))
        if not k:
            json.dump(dict(zip(names,v)),out, indent=1,separators=(',', ': '))
            out.write("\n")
 '''

