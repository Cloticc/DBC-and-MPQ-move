

import glob
import os
import shutil
src_folder = r"SPELL EDITOR EXPORT LOCATON"
dst_folder1 = r"DBC LOCATION"
dst_folder2 = r"DATA LOCATION"
pattern = "\*.mpq" and "\*.dbc"
files = glob.glob(src_folder + pattern)

for f in files:
    if f.endswith('.dbc'):
        shutil.copy(f, dst_folder1)
    elif f.endswith('.mpq'):
        shutil.copy(f, dst_folder2)
    else:
        print("File type not supported")

print("DBC files moved to: " + dst_folder1)
print("MPQ files moved to: " + dst_folder2)