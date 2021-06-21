#!/usr/bin/env python3

import sys, json, os
sys.path.append('../components')

from Block import Block
from Chain import Chain

# Membuat Blockchain Baru
filepath = "../store/mined"
chain = Chain().load(filepath)