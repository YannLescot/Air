from os import listdir

from os.path import isfile, join

fichiers = [f for f in listdir(Air) if isfile(join(Air, f))]

print(fichiers)