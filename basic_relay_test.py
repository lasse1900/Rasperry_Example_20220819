#!/usr/bin/python
'''*****************************************************************************************************************
    Seeed Studio Relay Board Example
    By John M. Wargo
    www.johnwargo.com
********************************************************************************************************************'''
from __future__ import print_function

import sys
import time

from relay_lib_seeed import *


def process_loop():
    # now cycle each relay every second in an infinite loop
    relay_on(1)
    relay_on(2)
    time.sleep(3)
    relay_off(1)
    relay_off(2)


# Now see what we're supposed to do next
if __name__ == "__main__":
    try:
        process_loop()
    except KeyboardInterrupt:
        # tell the user what we're doing...
        print("\nExiting application")
        # turn off all of the relays
        relay_all_off()
        # exit the application
        sys.exit(0)
