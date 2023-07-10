import os
import subprocess

eccodes_version = '2.30.2'
dir_name = f'eccodes-{eccodes_version}-Source'
url = f'https://confluence.ecmwf.int/download/attachments/45757960/eccodes-{eccodes_version}-Source.tar.gz?api=v2'

def call_command(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

call_command(['curl', '-o', 'sources.tar.gz', url])
call_command('7z x -tgzip -so sources.tar.gz | 7z x -si -ttar')