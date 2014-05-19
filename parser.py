import optparse, os
import test 
import glob
from color import *
from tempClass import *
import time

cl = getColor()
tmp = tempData()

try:

	def getGlobList(gpath):
   		gl = glob.glob(gpath)
    		return str(gl).strip("[]'")

	parser = optparse.OptionParser(version='0.01', description='Test folder parser')
	parser.add_option('-p','--path', type='string', action = "store", dest='path', help='Input path')


	options,arguments=parser.parse_args()

	for key,value in options.__dict__.items():
     		if(key == 'path'):
        		needed_path = value

	def dir_item_handler(info):
        	out = ""
        	for key in info:
                	out = "Path: %s, Size: %s, OwnerId: %s, Mode: %s, Time: %s, Type: %s " % (cl.getPathType(info["Path"], info["Type"]), info["Size"], info["OwnerId"], info["Mode"], info["Creating time"], cl.getTypeColor(info["Type"]))
        	print out 

	def tmp_item_handler(info):

		out = ""
        	for key in info:
                	out = "Path: %s, Size: %s, OwnerId: %s, Mode: %s, Time: %s, Type: %s " % (cl.getPathType(info["Path"], info["Type"]), info["Size"], info["OwnerId"], info["Mode"], info["Creating time"], cl.getTypeColor(info["Type"]))	

		tmp.writeToTmpFile(info)


    	glob_reverse = getGlobList(needed_path)
    	scanner = test.DirectoryScanner()
    	scanner.scan(glob_reverse, dir_item_handler)
    	#scanner.scan(glob_reverse, tmp_item_handler)
    	scanner.getPid()
	time.sleep(60)    
except OSError as e:
        print cl.redText('Exception error is: %s') % e
except KeyboardInterrupt:
        print cl.redText("Canceling operation.Exit")
        sys.exit(0)
