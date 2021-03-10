import os
import sys
import string
import re
import json


folderpath = '~/Desktop/artnet_articles/'
path = os.path.expanduser(folderpath)

filelist = os.listdir(path)

for name in filelist:
    newname = name.replace("-", "_")
    newname = newname.replace(";", "")

    newname = newname.replace(" ", "_")

    newname = newname.replace('#', '')
    newname = newname.replace('%', '')
    newname = newname.replace('*', '')
    newname = newname.replace('<', '')
    newname = newname.replace('>', '')
    newname = newname.replace('*', '')
    newname = newname.replace('?', '')

    newname = newname.replace("(", "")
    newname = newname.replace(")", "")
    newname = newname.replace("[", "")
    newname = newname.replace("]", "")
    newname = newname.replace("{", "")
    newname = newname.replace("}", "")

    newname = newname.replace("'", "")
    newname = newname.replace('"', "")

    newname = newname.replace(".", "_")
    newname = newname.replace(",", "")
    newname = newname.replace("+", "_")

    newname = newname.replace('_json' , '.json')
    filepath_origin = os.path.join(os.path.expanduser(folderpath), name)
    filepath_final = os.path.join(os.path.expanduser(folderpath), newname)

    try:
        os.rename(filepath_origin, filepath_final)
        print(newname)
    except FileNotFoundError:
        print("error:   " + name)

"""
    if newname != name:
        # print(path)
        #print(os.path.dirname(path.encode('utf8').decode(sys.stdout.encoding)) + "t" + os.path.basename(path.encode('utf8').decode(sys.stdout.encoding)) +
              "ttt -> " + os.path.basename(newname.encode('utf8').decode(sys.stdout.encoding)))
        os.rename(name, newname)


"""