import os
import pwd


r_id = os.getuid()

r_g_id = os.getgid()

name = pwd.getpwnam('root')

print "%s %s %s " % (name, r_id, r_g_id)
