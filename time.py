#!/usr/bin/python3

import time,os

class buffer(object):
	def __init__(self):
		self.line0 = ""
		self.line1 = ""
		self.line2 = ""
		self.line3 = ""
		self.line4 = ""
		self.line5 = ""
		self.line6 = ""
		self.line7 = ""
		self.line8 = ""

	def print_lines(self):
		print(self.line0)
		print(self.line1)
		print(self.line2)
		print(self.line3)
		print(self.line4)
		print(self.line5)
		print(self.line6)
		print(self.line7)
		print(self.line8)

	def clean(self):
		self.line0 = ""
		self.line1 = ""
		self.line2 = ""
		self.line3 = ""
		self.line4 = ""
		self.line5 = ""
		self.line6 = ""
		self.line7 = ""
		self.line8 = ""

class large_number:
	def __init__(self,n):
		self.n = n
		self.line0 = ""
		self.line1 = ""
		self.line2 = ""
		self.line3 = ""
		self.line4 = ""
		self.line5 = ""
		self.line6 = ""
		self.line7 = ""
		self.line8 = ""

	def add_str(self,i,stg):
		if i == 0:
			self.line0 = stg
		if i == 1:
			self.line1 = stg
		if i == 2:
			self.line2 = stg
		if i == 3:
			self.line3 = stg
		if i == 4:
			self.line4 = stg
		if i == 5:
			self.line5 = stg
		if i == 6:
			self.line6 = stg
		if i == 7:
			self.line7 = stg
		if i == 8:
			self.line8 = stg

	def add_to_buffer(self):
		buf.line0 += self.line0
		buf.line1 += self.line1
		buf.line2 += self.line2
		buf.line3 += self.line3
		buf.line4 += self.line4
		buf.line5 += self.line5
		buf.line6 += self.line6
		buf.line7 += self.line7
		buf.line8 += self.line8

def get_big_chars():
	global big_chars
	digits=open("digits.txt","r")
	dig = digits.read().split('\n')
	curr = 0
	j = 0
	big_chars = []
	for i in dig:
		if i == "0-":
			curr = "0"
			j = 0
			big_chars.append(large_number("0"))
		elif i == "1-":
			curr = "1"
			j = 0
			big_chars.append(large_number("1"))
		elif i == "2-":
			curr = "2"
			j = 0
			big_chars.append(large_number("2"))
		elif i == "3-":
			curr = "3"
			j = 0
			big_chars.append(large_number("3"))
		elif i == "4-":
			curr = "4"
			j = 0
			big_chars.append(large_number("4"))
		elif i == "5-":
			curr = "5"
			j = 0
			big_chars.append(large_number("5"))
		elif i == "6-":
			curr = "6"
			j = 0
			big_chars.append(large_number("6"))
		elif i == "7-":
			curr = "7"
			j = 0
			big_chars.append(large_number("7"))
		elif i == "8-":
			curr = "8"
			j = 0
			big_chars.append(large_number("8"))
		elif i == "9-":
			curr = "9"
			j = 0
			big_chars.append(large_number("9"))
		elif i == ":-":
			curr = ":"
			j = 0
			big_chars.append(large_number(":"))
		else:
			if j != 0:
				for k in big_chars:
					if k.n == curr:
						k.add_str(j-1,i)
		j += 1

def new_separator():
	global buf
	buf.line0 += "  "
	buf.line1 += "  "
	buf.line2 += "  "
	buf.line3 += "  "
	buf.line4 += "  "
	buf.line5 += "  "
	buf.line6 += "  "
	buf.line7 += "  "
	buf.line8 += "  "

def load_9_segment_cli(time_str): 
	global buf
	global big_chars
	for char in time_str:
		for i in big_chars:
				if char == i.n:
					i.add_to_buffer()
					new_separator()

def get_time_string(H,M,S):
	if H == True:
		h = time.localtime().tm_hour
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
	return str(h) + ":" + str(m) + ":" + str(s)

def main():
	global buf
	global big_chars

	buf = buffer()
	get_big_chars()
	for k in big_chars:
		print (k.line0)
		print (k.line1)
		print (k.line2)
		print (k.line3)
		print (k.line4)
		print (k.line5)
		print (k.line6)
		print (k.line7)
		print (k.line8+"\n")

	while True:
		time.sleep(0.1)
		os.system("clear")
		now = get_time_string(True,True,True)
		load_9_segment_cli(now)#, bitch!
		buf.print_lines()
		buf.clean()

if __name__ == '__main__':
	main()
