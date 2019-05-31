#! /usr/bin/python
import sys,os,csv

if len(sys.argv) < 2:
	sys.stderr.write("USAGE:%s csv-file\n"%sys.argv[0])
	sys.exit(1)

ifd = open(sys.argv[1],"r")
ofd = open(sys.argv[1][:-4]+".dat","w")

line = ifd.readline()
line = line.split(",")
fITD = float(line[2])
tITD = float(line[3])
step = float(line[4])
N    = int((tITD-fITD)/step)
line = line[6:]

list = map(None,[tITD - (float(x)*step) for x in xrange(N+1)],line)
list = list[:-1]
list.sort()
for mp in  list:
	ofd.write("%g\t%s\n"%mp)
ifd.close()
ofd.close()
