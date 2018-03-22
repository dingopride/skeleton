#!/usr/bin/env python
# skeleton
# Developed by acidvegas in Python
# https://git.supernets.org/acidvegas/skeleton
# functions.py

import re

import config

def is_admin(ident):
	return re.compile(config.settings.admin.replace('*','.*')).search(ident)
