#!/usr/bin/python
#-*- coding: utf-8 -*-
#Jasmin Engelmann
#11-747-334

import sys
import re
import nltk

filename = sys.argv[1]
infile = open(filename, 'r', encoding='utf-8')

with open('shakespeare_preprocessed_round2.txt', 'a', encoding='utf8') as outfile:
	#reads text into string
	text = infile.read()
	#removes empty lines
	text = "".join([s for s in text.strip().splitlines(True) if s.strip()])
	#tokenizes text on sentence level
	sent_text = nltk.sent_tokenize(text)

	for line in sent_text:
		#removes additional spaces
		line.lstrip(' ')
		#removes page numbers
		line = re.sub(r'\s+\d+', r'', line)
		#'inserts' space after each character
		line = ' '.join(line)
		#inserts <space> delimiter between words
		line = re.sub(r'  ', r' <space>', line)
		#removes extra spaces
		line = re.sub(r'(<space> )+', r'<space> ', line)
		#separates line by \n
		line = line + '\n'
	
		outfile.write(line)

infile.close()