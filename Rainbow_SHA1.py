#-----------------Libraries-------------------------
###System I.O Lib. Need to be Added for Later Usage
import hashlib

#-----------------Variables-------------------------

##Var. for Input File (No New Line -> tr -d '\n')
###Additional Code Required for Asking for User's Input
infile = '8H'

##Open Filestream (infile) / Append Mode
###Additional Code Required for Asking for User's Input
outfile = open("MD.txt","a")

#------------------SHA1_Hashing_Algorithm--------------
##Open Filestream (outfile) / Readonly Mode
with open(infile, "r") as inf:
    ##For Loop -> Read the File Line-by-Line
    for line in inf:

        ##Write SHA1 Hash Digest to the Output/ Strip(\n) / Ecnode(for Py3.x) / Newline
        outfile.write(hashlib.sha1(line.strip().encode('utf-8')).hexdigest()+'\n')












######

#print(line, end="")
#print (hashlib.md5(line.strip().encode('utf-8')).hexdigest())
