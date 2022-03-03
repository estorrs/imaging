"""
From https://gist.github.com/adamjtaylor/8955320b56012b7ddb3ab6597394d632
"""

#!/usr/bin/python

import argparse
import tifffile
import re

parser = argparse.ArgumentParser(
    description = 'Removes date, time, time zone, Scanscope ID, user and DSR ID tags from svs files'
)
parser.add_argument('input',
                    type=str,
                    help='the file to parse the headers of ')
parser.add_argument('--remove',
                    help='If set the tags are removed entirely',
                    action = 'store_true')
parser.add_argument('--redact',
                    type=str,
                    default= "REDACTED",
                    help='The string to replace values with,  Defaults to "REDACTED"')

args = parser.parse_args()

description = tifffile.tiffcomment(args.input)


pattern = r'\|(Date|Time Zone|ScanScope ID|User|Time|DSR ID) = ([^\|]+)'

if args.remove==True:
    replacement = ""
else:
    replacement = "|\\1 = " + args.redact 


description_clean = re.sub(pattern, replacement, description)

tifffile.tiffcomment(args.input, comment = description_clean)
