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

	def print_lines(self,str1):
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
	for char in time_str:
		if char == "0":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "##    ##"
			buf.line3 += "##    ##"
			buf.line4 += "##    ##"
			buf.line5 += "##    ##"
			buf.line6 += "##    ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()
		if char == "1":
			buf.line0 += "      ##"
			buf.line1 += "      ##"
			buf.line2 += "      ##"
			buf.line3 += "      ##"
			buf.line4 += "      ##"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "      ##"
			buf.line8 += "      ##"
			new_separator()
		if char == "2":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "      ##"
			buf.line3 += "      ##"
			buf.line4 += "########"
			buf.line5 += "##      "
			buf.line6 += "##      "
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()
		if char == "3":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "      ##"
			buf.line3 += "      ##"
			buf.line4 += "########"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()
		if char == "4":
			buf.line0 += "##    ##"
			buf.line1 += "##    ##"
			buf.line2 += "##    ##"
			buf.line3 += "##    ##"
			buf.line4 += "########"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "      ##"
			buf.line8 += "      ##"
			new_separator()
		if char == "5":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "##      "
			buf.line3 += "##      "
			buf.line4 += "########"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()
		if char == "6":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "##      "
			buf.line3 += "##      "
			buf.line4 += "########"
			buf.line5 += "##    ##"
			buf.line6 += "##    ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()#the game
		if char == "7":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "      ##"
			buf.line3 += "      ##"
			buf.line4 += "  ######"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "      ##"
			buf.line8 += "      ##"
			new_separator()
		if char == "8":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "##    ##"
			buf.line3 += "##    ##"
			buf.line4 += "########"
			buf.line5 += "##    ##"
			buf.line6 += "##    ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()
		if char == "9":
			buf.line0 += "########"
			buf.line1 += "########"
			buf.line2 += "##    ##"
			buf.line3 += "##    ##"
			buf.line4 += "########"
			buf.line5 += "      ##"
			buf.line6 += "      ##"
			buf.line7 += "########"
			buf.line8 += "########"
			new_separator()

		if char == ":":
			buf.line0 += "    "
			buf.line1 += " ## "
			buf.line2 += " ## "
			buf.line3 += " ## "
			buf.line4 += "    "
			buf.line5 += " ## "
			buf.line6 += " ## "
			buf.line7 += " ## "
			buf.line8 += "    "
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
	buf = buffer()

	while True:
		time.sleep(0.1)
		os.system("clear")
		now = get_time_string(True,True,True)
		load_9_segment_cli(now)#, bitch!

		buf.print_lines()
		buf.clean()

if __name__ == '__main__':
	main()
