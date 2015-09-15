#!/usr/bin/python3

import time,os,sys

class buffer(object):
	def __init__(self):
		self.lines = {0:"" ,1:"" ,2:"" ,3:"" ,4:"" ,5:"" ,6:"" ,7:"" ,8:"" }

	def print_lines(self):
		for i in self.lines:
			print(self.lines[i])

	def clean(self):
		for i in self.lines:
			self.lines[i] = ""

class large_number:
	def __init__(self,n):
		self.n = n
		self.lines = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:""}

	def add_str(self,i,stg):
		self.lines[i] = stg

	def add_to_buffer(self):
		for i in range(0,9):
			buf.lines[i] = buf.lines[i] + self.lines[i]

def get_big_chars():
	global big_chars
	digits=open("digits.txt","r")
	dig_in = digits.read().split('\n')
	curr = 0
	j = 0
	big_chars = {}
	
	for i in dig_in:
		if i[:1] == "-":
			curr = i[1:]
			j = 0
			big_chars[curr]=large_number(curr)
		else:
			if j != 0:
				big_chars[curr].add_str(j-1,i)
		j += 1

def new_separator():
	global buf
	for i in buf.lines:
		buf.lines[i] += " "

def load_to_buf(time_str): 
	global buf
	global big_chars
	for char in time_str:
		big_chars[char].add_to_buffer()
		new_separator()

def get_time_string(H,M,S,typeof):
	pm = False

	if H == True:
		h = time.localtime().tm_hour

		if h >=12:
			if typeof == 12:
				h = h-12
			pm = True
		if len(str(h)) == 1:
			h = "0"+str(h)

	if M == True:
		m = time.localtime().tm_min
		if len(str(m)) == 1:
			m = "0"+str(m)

	if S == True:
		s = time.localtime().tm_sec
		if len(str(s)) == 1:
			s = "0"+str(s)

	if typeof == 12 and pm == False:
		return str(h) + ":" + str(m) + ":" + str(s) + ":AM"
	if typeof == 12 and pm == True:
		return str(h) + ":" + str(m) + ":" + str(s) + ":PM"
	if typeof == 24:
		return str(h) + ":" + str(m) + ":" + str(s)
		

def main(argv):
	global buf
	global big_chars

	if len(argv) > 1:
		if (argv[1] == "12") or (argv[1] == "24"):
			time_format = int(argv[1])
		else:
			print ("usage: ./time.py clock_type(12 or 24)")
			exit()
	else:
		time_format = 24

	buf = buffer()
	get_big_chars()

	while True:
		time.sleep(0.1)
		os.system("clear")
		now = get_time_string(True,True,True,time_format)
		load_to_buf(now)#, bitch!
		print("\033[1;31m")
		buf.print_lines()
		print("\033[0m")
		buf.clean()

if __name__ == '__main__':
	main(sys.argv)
