#!/usr/bin/python
activate_this = '/var/www/whatdayisitinnz/whatdayisitinnz/whatdayisitinnz/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys
head, tail = os.path.split(os.path.abspath(__file__))
sys.path.insert(0, head)
from whatdayisitinnz import app as application