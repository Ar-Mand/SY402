import os
import hashlib
import datetime
path = '/'
BLOCK_SIZE = 65536
for roots,ds,fs, in os.walk(path):
	if "dev" in roots:
		continue
	elif "proc" in roots:
		continue
	
	elif "run" in roots:
		continue
	elif "sys" in roots:
		continue
	elif "tmp" in roots:
		continue
	elif "var/lib" in roots:
		continue
	elif "var/run" in roots:
		continue
	else:
		for i in fs: #gotta do this because 
			pots = '/'+ roots + '/' + i
			torri = hashlib.sha256()
			with open(i,'rb') as mint:
				minty = mint.read(BLOCK_SIZE)
				while len(minty) > 0:
					torri.update(minty)
					minty = mint.read(BLOCK_SIZE)
			with open('mylogs.txt','a') as logger:
				times = datetime.datetime.now()
				logger.write(roots+' '+str(torri.hexdigest())+' '+str(times))
	
	
	
#def hasher(filename):
	