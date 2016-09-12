import os
import os.path
import time

rootdir = "F:\\Hades\\social\\7days"
want = "—Ó¿Ω"

for parents, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
                path = os.path.join(parents, filename)
                f = open(path, "r")
                lines = f.readlines()

                for line in lines:
                        if want in line:
                                print line

                
                
