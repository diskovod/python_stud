import os

class getProcPid(oblect):
    def __init__(self):
        pass

    def procId(self, pid):
        tmp_path = "/tmp"
        curr_pid = os.getpid()
        wp_f = open(wp + "/"+"myprocess.pid", "r+")
        wp_f.write("Pid: %s, Working Path: %s" % (str(curr_pid), str(wp)))
        wp_f.seek(0)
        r = wp_f.read()
        print r
        wp_f.close()

