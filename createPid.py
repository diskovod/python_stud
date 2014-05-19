import os

if os.path.exists("/var/run/myscript.pid"):
    f = file("/var/run/myscript.pid", "r+")
    curr_pid = os.getpid()
    f.write(str(curr_pid))
    print f.name
else:
     f = file("/var/run/myscript.pid", "w")
