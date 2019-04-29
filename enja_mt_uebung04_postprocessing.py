#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import re

filename = sys.argv[1]
infile = open(filename, 'r', encoding='utf-8')

#with open('shakespeare_postprocessed2.txt', 'a', encoding='utf-8') as outfile:
with open('shakespeare_postprocessed_round2.txt', encoding='utf-8') as outfile:

	for line in infile:
		#replace <eos> with \n
		line = re.sub(r'<eos>', r'', line)
		#remove whitespaces
		line = re.sub(r' ', r'', line)
		#replace <space> delimiter with whitespace
		line = re.sub(r'<space>', r' ', line)

		outfile.write(line)

infile.close()
