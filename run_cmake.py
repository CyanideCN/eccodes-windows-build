import os
import subprocess

cwd = os.getcwd()
build_path = os.path.join(cwd, os.environ['ECCODES_SOURCE_DIR'], 'build')
os.makedirs(build_path)
os.chdir(build_path)
subprocess.call('cmake -G "NMake Makefiles"',
            '-D CMAKE_INSTALL_PREFIX=${{ env.install_dir }}',
            '-D CMAKE_BUILD_TYPE=Release',
            '-D ENABLE_FORTRAN=0',
            '-D ENABLE_PYTHON=0',
            '-D ENABLE_NETCDF=0',
            '-D ENABLE_PNG=1',
            '-D ENABLE_JPG=1',
            '-D OPENJPEG_INCLUDE_DIR=${{ env.conda_dir }}\Library\include\openjpeg-2.5.0',
            '-D IEEE_LE=1',
            '-D ENABLE_EXAMPLES=0',
            '-D ENABLE_MEMFS=0',
            '-D ENABLE_TESTS=0',
            '-D ENABLE_EXTRA_TESTS=OFF', shell=True, stdout=subprocess.PIPE)