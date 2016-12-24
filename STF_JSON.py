#!/usr/local/bin/python3
# Convert stf transmittal in a Json file
# Revision 2016-12-12
# Copyright (c) 2016 Jeremy Heyl and Elisa Antolini


from subprocess import call
import json
import re


### UNCOMMENT THIS FOR GENERATE THE CSV output file from the Transmittal ####

#call('depth -v LMBX_cat.stf > DepthOut.csv', shell=True)



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
            else:
                if (currentlevel<minuspos):
                    f.seek(-len(line),1)
                    newdict=jparseFile(f)
                    line.strip()
                    line = line.strip(' ')
                    line = line.strip('-')
                    line = line.strip(' ')
                    line = line.strip('\n')
                    
                    dict[line]=newdict
                else:
                    f.seek(-len(line),1)
                    return dict
        else:
            key,content = CleanString(line)
            dict[key]=content
    
    return dict

#------------------------------------------------------------------------------
# main
#
def main():
    """
    This is the main routine.
    """


fname = open('DepthOut.csv','r')

Dictionary = jparseFile(fname)

with open('STFDepthOut.json', 'w') as outfile:
    json.dump(Dictionary, outfile, indent = 2)

#------------------------------------------------------------------------------
# Start program execution.
#
if __name__ == '__main__':
    main()

