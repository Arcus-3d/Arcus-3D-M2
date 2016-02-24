#!/usr/bin/python

import sys
import os
import subprocess
import importlib
import argparse
from time import *
from machinekit import launcher
from machinekit import config

launcher.register_exit_handler()
#launcher.set_debug_level(5)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
c = config.Config()
os.environ["MACHINEKIT_INI"] = c.MACHINEKIT_INI

try:
    launcher.check_installation()
    launcher.cleanup_session()
    launcher.load_bbio_file('cramps_cape.bbio')
    launcher.install_comp('reset.comp')
    launcher.start_process("configserver -n Arcus-3D-M1 ./lib/Arcus-Machineface")
    launcher.start_process('linuxcnc Arcus-3D-M1.ini')
except subprocess.CalledProcessError:
    launcher.end_session()
    sys.exit(1)

while True:
    sleep(1)
    launcher.check_processes()
