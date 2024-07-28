#!/usr/bin/env python3

import csv
import sys

iconsdef = csv.reader(sys.stdin)

# Skip header line
next(iconsdef)

for entry in iconsdef:
    name, devicon, url = entry

    svgurl = f'https://cdn.jsdelivr.net/gh/devicons/devicon@2.16.0/icons/{
        devicon}/{devicon}-original.svg'

    print(f'<a href="{url}" target="_blank" rel="noreferrer">')
    print(f'<img alt="{name}" src="{svgurl}" width="40" height="40"></img>')
    print('</a>')
