#!/usr/local/bin/python3

import os
import sys
import shutil

from subprocess import call

from itertools import groupby
import json


### UNCOMMENT THIS FOR GENERATE THE CSV output file from the Transmittal ####
#call('depth -v LMBX_cat.stf > DepthOut.csv', shell=True)


### This is a csv file version shorter than the original one, just for made a trial ####

fname = 'DepthOutProva.csv'

x=[]

#### Read the csv file generated from Depth command #####


with open(fname) as f:
    content = f.readlines()

for k in range(len(content)) :
    
    ### Split each rows in two contribution, when necessary ####
    
    for j in content[k]:
        
        if j == ":":
            line  = content[k]
            Indexline = line.index(":")-1
            
            
            if line[Indexline] != "[" :
                x.append(content[k].rsplit(':', 1)[0]) ## Will contain the strings before ':' character
               
                content[k] = line[line.find(':')+1 :  ] ## Will contain the strings after ':' character


            #print(content[k])




### This is the data format for create a JSON file with the same tree structure of the STF file ####

dataDic ={content[0]:{x[0]:content[1],x[1]:content[2],x[2]:content[3],x[3]:content[4],x[4]:content[5],x[5]:content[6],x[6]:content[7],x[7]:content[8],x[8]:content[9],x[9]:content[10],x[10]:content[11],x[11]:content[12],x[12]:content[13],content[14]:{content[15]:{x[13]:content[16], x[14]:content[17],x[15]:content[18],x[16]:content[19],x[17]:content[20],x[18]:content[21],x[19]:content[22],x[20]:content[23],x[21]:content[24],x[22]:content[25]},content[26]:{content[27]:{content[28]:{ x[23]:content[29],x[24]:content[30],x[25]:content[31]}}, content[32]:{x[26]:content[33]}, content[34]:{x[27]:content[35],x[28]:content[36],x[29]:content[37],x[30]:content[38] }  }}}}

### Generate the JSON file ###

with open('STFDepthOut.json', 'w') as outfile:
    json.dump(dataDic, outfile, indent=4)





'''
with open("DepthOut.csv") as f, open("STFDepthOut.json","w") as out:
    
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

