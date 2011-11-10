import sys, os, subprocess, glob

def testOrgs(subdir):
	"""
	Run a verilog test suite in a subdirectory.
	Assumes the test suite is named test in test.v
	test.v should output a "correct" or "wrong" line for each successful/failed test.
	"""
	outfile = open(file[:-1]+'txt', 'w')
	
	for file in glob.glob(os.path.join(subdir+'\\', '*.v')):
		print 'Testing organism ' + file
		subprocess.call(['iverilog', '-o',  file[:-1]+'o', file])
		process = subprocess.Popen(['vvp', file[:-1]+'o'], stdout=subprocess.PIPE)
		output = process.communicate() #(stdout, stderr)
		simResult = getSimulationResultsFromText(output[0])
		
	

if __name__ == "__main__":
	testOrgs(sys.argv[1])