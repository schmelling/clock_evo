#!/usr/bin/python
import os
import sys
from subprocess import call

#Figure out the directory name to save to
if len(sys.argv) != 3:
	print "Usage: python runAvida.py <OUTPUT_DIRECTORY> <RANDOM_SEED>"
	quit()

outDir = sys.argv[1]
randomSeed = sys.argv[2]

#Make sure the entire path exists, or else avida won't actually save
#even though it will create the inner-most dir if everything else exists
if not os.path.exists(outDir):
	os.makedirs(outDir)

#Run Avida i times, setting the output directory to data-i where i is the current run number
call(["avida", "-c", "avida.cfg",  "-set", "DATA_DIR", outDir, "-set", "RANDOM_SEED", randomSeed])
