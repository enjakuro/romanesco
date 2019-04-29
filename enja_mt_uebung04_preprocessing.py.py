#!/usr/bin/python
#-*- coding: utf-8 -*-
#Jasmin Engelmann
#11-747-334

import sys
import re

filename = sys.argv[1]
infile = open(filename, 'r', encoding='utf-8')

with open('shakespeare_preprocessed.txt', 'a', encoding='utf8') as outfile:

	for line in infile:
		#'inserts' space after each character
		line = ' '.join(line)
		#inserts <space> delimiter between words
		line = re.sub(r'  ', r' <space>', line)

		outfile.write(line)


infile.close()