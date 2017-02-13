#!/usr/bin/python

#Simple utility to generate the complex pool creation job file and submit it
#for all 40 populations

#Command line argument:
#1: the output directory

import sys
import os
import subprocess

if len(sys.argv) != 2:
	print "Usage: python submit.py <OUTPUT_DIR>"
	quit()

outputDir = sys.argv[1]

if not os.path.exists(outputDir):
	os.makedirs(outputDir)

for i in range(1, 51):
	#Create the  qsub file
	jobScript = open("pool%s.qsub" %i, "w")

	jobScript.write("#!/bin/bash -login\n")
	jobScript.write("#PBS -l walltime=06:00:00,nodes=1:ppn=1,mem=4gb\n")
	jobScript.write("#PBS -j oe\n")
	jobScript.write("#PBS -N pool%s\n\n" %i)

	jobScript.write("#Load the Avida module\n")
	jobScript.write("module load avida\n\n")

	jobScript.write("#Change to your working directory\n")
	jobScript.write("cd %s\n" %os.path.abspath("."))

	jobScript.write("#Run the Avida script\n")
	jobScript.write("python runAvida.py %s/tmp%s i\n\n" %(outputDir, i))

	#Go ahead and copy the org over and remove the temp directory
	jobScript.write("#Copy the organism over and delete the temp dir\n")
	jobScript.write('for f in %s/tmp%s/*.dat; do cp "$f" %s/run-%s-"${f##*/}"; done\n' %(outputDir, i, outputDir, i))
    jobScript.write("rm -rf %s/tmp%s\n" %(outputDir, i))

	jobScript.close()

	#Now submit the job script we just created
	subprocess.call(["qsub", "pool%s.qsub" %i])
