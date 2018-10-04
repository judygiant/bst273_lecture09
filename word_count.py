#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

"""parser.add_argument(
	"arg",
	help="what does this do?",
)"""
parser.add_argument(
"data_file",
help="path to the file we want to read"
)
args=parser.parse_args()
print (args.data_file)
fh = open(args.data_file)
print("the file handle is", fh)
#-------------------------------------------------------------------------------
nlines=0
nwords=0
nchars=0
for line in fh:
	nlines +=1
	wds= line.strip().split(" ")
	nwords += len(wds)
	nchars += len(line)

print ("lines",nlines, "words", nwords, "characters", nchars)

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
