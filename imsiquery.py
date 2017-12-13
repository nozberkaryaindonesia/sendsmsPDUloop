#!/usr/bin/env python

import sys
import sqlite3
import os

#./OpenBTSCLI sendsms nomorimsi nomorpengirim isisms

if len(sys.argv) < 4:
	print "Usage : ./imsiquery.py database nomorpengirim isisms"
	print 'Contoh: ./imsiquery.py scanimsi_513.db 123456 "ini test sms"'
	sys.exit()

db = sqlite3.connect(sys.argv[1])
file = "%s.sh" % sys.argv[2]
f = open(file,'w')
cursor = db.cursor()
for row in db.execute('SELECT imsi FROM observations'):
	s = './OpenBTSCLI sendsms %s %s "%s"\n' % (row[0].replace(" ",""), sys.argv[2], sys.argv[3])
	f.write(s)
f.close()
os.chmod(file, 493)	

