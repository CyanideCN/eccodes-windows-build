import os
import subprocess

cwd = os.getcwd()
with open('ECCODES_SOURCE_DIR', 'r') as f:
    source_dir = f.read().strip()
build_path = os.path.join(cwd, source_dir, 'build')
print(build_path)
os.makedirs(build_path)
os.chdir(build_path)
subprocess.call('cmake -G "NMake Makefiles"',
            '-D CMAKE_INSTALL_PREFIX=C:\eccodes',
            '-D CMAKE_BUILD_TYPE=Release',
            '-D ENABLE_FORTRAN=0',
            '-D ENABLE_PYTHON=0',
            '-D ENABLE_NETCDF=0',
            '-D ENABLE_PNG=1',
            '-D ENABLE_JPG=1',
            '-D OPENJPEG_INCLUDE_DIR=C:\Miniconda\Library\include\openjpeg-2.5.0',
            '-D IEEE_LE=1',
            '-D ENABLE_EXAMPLES=0',
            '-D ENABLE_MEMFS=0',
            '-D ENABLE_TESTS=0',
            '-D ENABLE_EXTRA_TESTS=OFF', shell=True, stdout=subprocess.PIPE)