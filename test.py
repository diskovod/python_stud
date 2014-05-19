import os
import datetime
import sys
import decimal
import glob

class DirectoryScanner(object):
    def __init__(self):
        pass

    def getSizeStr(self, size):
        lst = ['B', 'Kb', 'Mb', 'Gb', 'Tb']
        remnant = float(size)
        counter = 0
    
        while int(remnant) > 1024:
            remnant = remnant/1024.0 
            counter = counter + 1
            if counter == (len(lst)-1):
                break
    
        return format(remnant,'.2f') + " " + lst[counter]
    
    def getType(self, path):
        if(os.path.isfile(path) == True):
            return "file"
        elif (os.path.isdir(path) == True):
            return "dir"
        elif (os.path.islink(path) == True):
            return "link"
        return "unkn"
    
    def getModeStr(self, mode):
        return str(oct(mode)[-3:])
    
    def getTimeStr(self, time):
        return str(datetime.datetime.fromtimestamp(time))

    def getOwnerId(self, ownerId):
        return str(ownerId)
	
    def getWorkingPath(self):
	print os.path.dirname(os.path.realpath(__file__))

    def getPid(self):
	wp = os.path.dirname(os.path.realpath(__file__))
	curr_pid = os.getpid()

        if os.path.exists(str(wp) +"/"+"mysript.pid"):
	    wp_f = file(str(wp) + "/"+"myscript.pid", "r+")
	    wp_f.write("Pid: %s, Working Path: %s" % (str(curr_pid), str(wp)))
	    current_file = open(wp_f)
	    r = current_file.read()
	    print r
	    wp_f.close()
	    	
        else:
	    wp_f = file(str(wp) + "/"+"myscript.pid", "w+")
            wp_f.write("Pid: %s, Working Path: %s" % (str(curr_pid), str(wp)))
	    current_file = open(str(wp_f))
            r = current_file.read()
            print r
            wp_f.close()
	      
    def getFileInfoStr(self, path_to_file):
        stats = os.stat(path_to_file)
    
        fileInfo = {"Path" : path_to_file, \
                "Size": self.getSizeStr(stats.st_size), \
                "OwnerId": self.getOwnerId(stats.st_uid), \
                "Mode": self.getModeStr(stats.st_mode), \
                "Creating time": self.getTimeStr(stats.st_mtime), \
                "Type": self.getType(path_to_file) }
    
        return fileInfo
    
    def scan(self, path, handler):
        for file in os.listdir(path):
            filepath = path + file
    
            fileInfo = self.getFileInfoStr(filepath)
            
    
            handler(fileInfo)
