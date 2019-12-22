#!/usr/bin/python2.7
#Author by Muhammad Rendy Iswardi
#CodeName: Sterben404
#09 Desember 2019

import os,re,time,sys
import requests
import urllib2
import ssl
import threading

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[36m'
purple = '\033[35m'
reset = '\033[0m'
#initialize OS for display clear
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass
#runningText
def write(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.00100)
#Banner
print(green+"   ______       ____  _______           __          ")
print("  / __/ /  ___ / / / / ___/ /  ___ ____/ /_____ ___ ")
print(" _\ \/ _ \/ -_) / / / /__/ _ \/ -_) __/  '_/ -_) __/")
print("/___/_//_/\__/_/_/  \___/_//_/\__/\__/_/\_\\__/_/   ")
write(blue+"Author by Sterben404 - Moch Rendy"+yellow)
print(red+'( For List Shell use http:// )')

#Main
def main(open_shell):
	for show in open_shell:
		try:
			header = {'Content-Type' : 'text/html; charset=UTF-8','User-Agent':''}
			req = urllib2.Request(show, headers=header)
			r = urllib2.urlopen(req, context=ssl._create_unverified_context())
			r.code
			print(green+"[ LIVE ] "+reset+show)
			with open('live.txt','a') as live:
				live.write(show+'\n')
				live.close()
		except:
			print(red+"[ DIE  ] "+reset+show)
			with open('die.txt', 'a') as die:
				die.write(show+'\n')
				die.close()
			pass

def cekfile():
	try:
		open(shell, 'r')
	except IOError as e:
		write(red+'[ ! ]%s File Not Found!' % reset)
		exit()
	pass

#Input
write(yellow+"LIVE Shell : %s live.txt" % green)
write(yellow+"DIE Shell  : %s die.txt" % red+reset)
if __name__ == "__main__":
	shell = raw_input('List Shell :  '+blue)
	cekfile()
	target	= [i for i in open(shell).read().split("\n") if i != ""]
	t = threading.Thread(target=main, args=(target, ))
	t.start()
