from os import listdir, system
from os.path import isfile, join

import random
import commands

#mypath = "/home/82035644020/Documentos/Imagens/wallpapers"
mypath = "/home/82035644020/.config/wallpapers"
images = [f for f in listdir(mypath) if isfile(join(mypath, f))]

i = random.randint(0, len(images)-1)

cmd = "pcmanfm --set-wallpaper={0}/{1} ".format(mypath, images[i])

#print cmd
#--wallpaper-mode=stretch

system(cmd)


