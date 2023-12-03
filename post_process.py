import shutil
import os

ori_dir = 'C:/Miniconda/envs/build/Library/bin'
dst_dir = 'C:/eccodes/bin'

for f in ['openjp2.dll', 'libpng16.dll', 'zlib.dll', 'netcdf.dll',
          'mfhdf.dll', 'hdf5_hl.dll', 'hdf5.dll', 'zip.dll']:
    print(f'Moving {os.path.join(ori_dir, f)}')
    shutil.copy2(os.path.join(ori_dir, f), dst_dir)

# Make archive
print(shutil.make_archive('eccodes-win-x64', 'zip', 'C:/eccodes'))