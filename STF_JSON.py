#!/usr/local/bin/python3
# Convert stf transmittal in a Json file
# Revision 2016-12-12
# Copyright (c) 2016 Jeremy Heyl and Elisa Antolini



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
                # print(str(currentlevel)+" "+str(line))
            
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

filename = sys.argv[1]
print "******************************************************"
print("Input File = " +str(filename))

if not filename.endswith('.json'):
    
    # The input File is a Sedris Transmittal
    if filename.endswith('.stf'):

        jsonOutFile = filename.replace('.stf','.json')
        cmd = ['depth','-v',filename]

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    
        StfOut = proc.stdout.read()
        StfOut = StfOut.decode("utf-8")
        StfOut = StfOut.split("\n")
        StfOut = StfOut[7:len(StfOut)-14]
        StfOut = '\n'.join(StfOut)
        StfOut = StfOut.encode("utf-8")
        content = cStringIO.StringIO(StfOut)

     # The input file is not a Sedris Transmittal
    else:
        content = open(filename,'r')
        ext = filename[filename.find('.')+1 :  ] ## Will contain the strings after ':' character
        ext = '.'+ext
        jsonOutFile = filename.replace(ext,'.json')



    print("Output File = "+str(jsonOutFile))
    print "******************************************************"
    print "\n"
    Dictionary = jparseFile(content)

    with open(jsonOutFile, 'w') as outfile:
        json.dump(Dictionary, outfile, indent = 2)

else :
    print "\n"
    print "*********************** ERROR ************************"
    print "A json file cannot be converted into another json file"
    print "******************************************************"
    print "\n"

#------------------------------------------------------------------------------
# Start program execution.
#


if __name__ == '__main__':
    main()
