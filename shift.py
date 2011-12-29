"""
Script to change the offset of subtitle file.

USAGE: python shift.py offset_in_sec < infile.srt > outfile.srt
"""

import sys
from datetime import datetime, timedelta

DELTA = int(sys.argv[1])

def shift_time(ts):
	return (datetime.strptime(ts, '%H:%M:%S,%f') + timedelta(seconds=DELTA)).strftime('%H:%M:%S,%f')[:12]

for s in sys.stdin.readlines():
	if '-->' in s:
		ts1, _, ts2 = s.split()
		ts1 = shift_time(ts1)
		ts2 = shift_time(ts2)
		print '%(ts1)s --> %(ts2)s' % locals()
	else:
		print s.strip()
