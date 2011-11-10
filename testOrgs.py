import sys, os, subprocess, glob

def testOrgs(subdir):
	"""
	Run a verilog test suite in a subdirectory.
	Assumes the test suite is named test in test.v
	test.v should output a "correct" or "wrong" line for each successful/failed test.
	"""
	for file in glob.glob(os.path.join(subdir+'\\', '*.v')):
		print "Testing organism " + file
		subprocess.call(["iverilog", "-o",  file[:-1]+'o', file])
	

if __name__ == "__main__":
	testOrgs(sys.argv[1])