import os, sys
import arabic_reshaper
from bidi.algorithm import get_display

# Main folder path
dir_path = os.path.join(sys.path[0])

# list to store files

extra_c_dir = os.path.join(dir_path, 'files') # the directory of the files that contains the extra characters
extra_c = []

# Iterate directory

for path in os.listdir(extra_c_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(extra_c_dir, path)): 
        extra_c.append(path)
print(extra_c)

for i in extra_c:
    with open(os.path.join(extra_c_dir, i), "r", encoding = "utf-8") as f:
        print(i)
        if i == 'prefix.txt':
            d = f.readlines()
            prefix = []
            for t in d:
                prefix.append(get_display(arabic_reshaper.reshape(t[:-1])))

        elif i == 'suffix.txt':
            d = f.readlines()
            suffix = []
            for t in d:
                suffix.append(get_display(arabic_reshaper.reshape(t[:-1])))
            
print(prefix)
print(suffix)