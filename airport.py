#!/usr/bin/python
# -*- encoding: utf-8 -*-
__description__ = 'A WiFi Perimeter scanner for OSX'
__author__ = 'Luis Rodil-Fernandez <root@derfunke.net>'
__version__ = '0.1.1'

"""
Before running this script make sure that the airport executable is in your path. Create a symlink to it like this:

$ sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/sbin/airport
$ airport --scan --xml
"""
import sys, os
import re, requests
import logging
import subprocess
from pprint import pprint
from OSC import *

try:
    import plistlib
    PLISTLIB_IS_IMPORTED = True
except ImportError:
    print(u"DEBUG: Cannot import the plistlib lib. I may not be able to properly parse a binary pblist")


ROOT_PATH = "/"
DEFAULT_HOST_ADDRESS = ("127.0.0.1", 2222)  # host, port tuple


def parse_airport_history():
    """ Look into the airport preferences files where OSX saves all the WiFi network that the device has ever been connected to """
    path = os.path.join(ROOT_PATH, "Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist")

    try:
        plist = plistlib.readPlist(path)
        pprint(plist)
    except (IOError):
        logging.error(u"Cannot open " + path , "ERROR")


def scan():
    """ Use the OSX provided airport utility to obtain wireless AP that are currently in range """
    p = subprocess.Popen(['airport', '--scan', '--xml'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    plistdict = plistlib.readPlistFromString(out)
    print("*"*80)
    #pprint(plistdict)
    retval = []
    for i in plistdict:
        #print("{0} {1} {2}".format(i['SSID_STR'], i['RSSI'], i['BSSID']))
        #pprint(i)
        retval.append({"SSID":i['SSID_STR'], "MAC":i['BSSID'], "RSSI":i['RSSI']})
    return retval


if __name__ == '__main__':
    logging.getLogger().handlers = []
    logging.basicConfig(level=logging.DEBUG)
    main()
    #parse_airport_history()
    #scan()
