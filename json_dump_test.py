import json
import tempfile
import os, glob

for filename in os.listdir("/media/sf_CentOs/"):
    if filename.startswith('tmpParseData'):
        os.remove(filename) 

dirname, basename = os.path.split('tmpParseData')
f = tempfile.NamedTemporaryFile(prefix=basename, dir=dirname, delete=False)
#fname = temp.name
#obj_json = u'{"answer": [42.2], "abs": 42}'
#json_test = json.loads(obj_json)
#print(json_test)
#print("Saving...\n")
#json.dump(json_test, temp)
#temp.close()
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

json.dump(data, f)
f.flush()
f.seek(0)

print(json.load(f))
