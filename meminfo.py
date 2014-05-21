import re
from test import *
import os

load_av = os.getloadavg()
test_cl = DirectoryScanner()
 
 
def get_meminfo():
 
    re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')
    pattern = re.compile(r'^(\w+):\s*(\d+)\skB')	
    result = dict()
    for line in open('/proc/meminfo'):
        match = pattern.match(line)
        if not match:
            continue # skip lines that don't parse
        key, value = match.groups(['key', 'value'])
        result[key] = int(value)
    return result

def getUsedMemoryPercent(res):
	
	free = res["MemFree"]
	total = res["MemTotal"]
	free_perc = free*100/total
	used_perc = 100 - free_perc
	
	return used_perc

def getUsedMemory(res):
	
	free = res["MemFree"]
        total = res["MemTotal"]

	used_kb = total - free
	used_mb = test_cl.getSizeStr(used_kb)

	return used_mb

def getUsedSwap(res):
	
	free = res["SwapFree"]
        total = res["SwapTotal"]

        used_kb = total - free
        used_mb = test_cl.getSizeStr(used_kb)

        return used_mb

def getUsedSwapPercent(res):

	free = res["SwapFree"]
        total = res["SwapTotal"]
        free_perc = free*100/total
        used_perc = 100 - free_perc

        return used_perc

def getLoadAvarage():
	
	load_av = os.getloadavg()
	str_av = str(load_av)
	pattern = "^\((\d+.\d+),\s*(\d+.\d+),\s*(\d+.\d+)"
	prog = re.compile(pattern)
	result = prog.match(str_av)
	
	fin_res = {'min':result.group(1), 'f_min':result.group(2), 'ft_min':result.group(3)}
	
	return fin_res


	
memInfo = get_meminfo()
usedMemPerc = getUsedMemoryPercent(memInfo)
usedMem = getUsedMemory(memInfo)
usedSwapPerc = getUsedSwapPercent(memInfo)
usedSwap = getUsedSwap(memInfo)
loadAv = getLoadAvarage()

print loadAv

#print """ Used Memory: %s/%s%%  \n Used Swap: %s/%s%% \n Load Avarage: %s""" % (usedMem, usedMemPerc, usedSwap, usedSwapPerc, load_av)






