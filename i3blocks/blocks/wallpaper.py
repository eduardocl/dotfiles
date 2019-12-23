from os import listdir, system, path
from os.path import isfile, join

import random
import commands

mypath =  path.expanduser("~/.config/wallpapers")
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i = random.randint(0, len(images)-1)
cmd = "feh --bg-fill {0}/{1} ".format(mypath, images[i])
system(cmd)
print " "

