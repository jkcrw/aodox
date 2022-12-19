#!/usr/bin/env python3
"""Copy firmware into correct location for qmk"""

import os
import shutil

from pathlib import Path

source = Path(__file__).parents[0]
dest = source.parents[0] / 'qmk_firmware/keyboards/aodox'
shutil.copytree(source, dest, dirs_exist_ok=True)

print('\ncopying firmware...done\n')
print(f'source: {source}')
print(f'dest: {dest}')
