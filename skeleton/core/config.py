#!/usr/bin/env python
# skeleton
# Developed by acidvegas in Python
# https://git.supernets.org/acidvegas/skeleton
# config.py

class connection:
	server     = 'irc.server.com'
	port       = 6667
	proxy      = None
	ipv6       = False
	ssl        = False
	ssl_verify = False
	vhost      = None
	channel    = '#dev'
	key        = None

class cert:
	key      = None
	file     = None
	password = None

class ident:
	nickname = 'DevBot'
	username = 'devbot'
	realname = 'git.supernets.org/acidvegas'

class login:
	network  = None
	nickserv = None
	operator = None

class throttle:
	command   = 3
	reconnect = 10
	rejoin    = 3

class settings:
	admin    = 'nick!user@host.name' # Must be in nick!user@host format (Can use wildcards here)
	cmd_char = '!'
	log      = False
	modes    = None
