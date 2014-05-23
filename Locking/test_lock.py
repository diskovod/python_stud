import fcntl

#lockfile = "/media/sf_CentOS/python_stud/myscript.pid"

def lockFile(lockfile):
    fp = open(lockfile, 'r')
    try:
        fcntl.lockf(fp, fcntl.LOCK_EX)
    except IOError:
        return False

    return True


lockfile = "/media/sf_CentOS/python_stud/myscript.pid"
lockFile(lockfile)
