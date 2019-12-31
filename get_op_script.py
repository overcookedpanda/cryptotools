#!/usr/bin/env python3
import sys
from btctools import *
address = sys.argv[1]
script = address_to_script(address)
print(script.hex())

