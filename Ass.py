#!/usr/bin/python

import socket
import socks
import sys
import argparse
import os
from time import sleep
import requests

parser = argparse.ArgumentParser()
parser.add_argument('host',help='Host you want to scan')
args = parser.parse_args()
ip = args.host
def logo():
	print "\033[1;33m  ____  _____ _____\033[0m"
	print "\033[1;33m /    |/ ___// ___/\033[0m"
	print "\033[1;33m|  o  (   \_(   \_ \033[0m"
	print "\033[1;33m|     |\__  |\__  |\033[0m"
	print "\033[1;33m|  _  |/  \ |/  \ |\033[0m"
	print "\033[1;33m|  |  |\    |\    |\033[0m"
	print "\033[1;33m|__|__| \___| \___|\033[0m \n"
	print "    \033[1;42mBy Black Leader\033[0m"

os.system('clear')
logo()
try:
	print "\033[1;33m\n[*] Wait few secound to start tor service....\033[0m"
	os.system('service tor restart')
	sleep(3)
	print "\033[1;32m[*] connect tor ....\033[0m"
	socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
	socket.socket = socks.socksocket
	print (requests.get('http://icanhazip.com')).content
	print "\033[1;32m[*] connect tor success :\033[0m"
except:
	print "\033[1;31m[-] connect tor failed ."
	
flag = 1

open_ports = []

common_ports = {
	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}

t = "\n[+] Scanning ports on : "+str(ip)+"\n"

for char in t:
	sleep(0.04)
	sys.stdout.write("\033[93m"+char+"\033[0m")
	sys.stdout.flush()

def check_port(ip, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip, port))
		if r == 0:
			result = r
		sock.close()
	except Exception, e:
		pass
	return result

def get_service(port):
	port = str(port)
	if port in common_ports:
		return common_ports[port]
	else:
		return 0

try:
	l = "[+] Scan in progress..\n"
	for char in l:
		sleep(0.04)
		sys.stdout.write("\033[1;32m"+char+"\033[0m")
		sys.stdout.flush()
	y = "[+] Connecting to Port : \n"
	for char in y:
		sleep(0.04)
		sys.stdout.write("\033[1;32m"+char+"\033[0m")
		sys.stdout.flush() ,
	if flag:
		for p in sorted(common_ports):
			sys.stdout.flush()
			p = int(p)
			response = check_port(ip, p)
			if response == 0:
				open_ports.append(p)

	a = "\n=========================================\n"
	for char in a:
		sleep(0.04)
		sys.stdout.write("\033[1;32m"+char+"\033[0m")
		sys.stdout.flush()
	c ="\tScan Report : "+ip
	for char in c:
		sleep(0.04)
		sys.stdout.write("\033[93m"+char+"\033[0m")
		sys.stdout.flush()

	b = "\n=========================================\n"
	for char in b:
		sleep(0.04)
		sys.stdout.write("\033[1;32m"+char+"\033[0m")
		sys.stdout.flush()

	if open_ports:
		d = "Open Ports: \n"
		for char in d:
			sleep(0.04)
			sys.stdout.write("\033[93m"+char+"\033[0m")
			sys.stdout.flush()
		for i in sorted(open_ports):
			service = get_service(i)
			if not service:
				service = "Unknown service"
			print "\t"+str(i),service+ "\033[1;32m : Open\033[0m"
	else:
		print "Sorry, No open ports found.!!"

		os.system('service tor stop')
except KeyboardInterrupt:
	print "You pressed Ctrl+C. Exiting "
	sys.exit(1)
