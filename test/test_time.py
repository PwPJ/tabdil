import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_second():
	assert tabdil.time.second(('w', 2)) == 1209600
	assert tabdil.time.second(('d', 5)) == 432000
	assert tabdil.time.second(('H', 10)) == 36000
	assert tabdil.time.second(('m', 13)) == 780
	assert tabdil.time.second(('S', 987654321)) == 987654321

def test_minute():
	assert tabdil.time.minute(('w', 2)) == 20160
	assert tabdil.time.minute(('d', 5)) == 7200
	assert tabdil.time.minute(('H', 10)) == 600
	assert tabdil.time.minute(('m', 13)) == 13
	assert tabdil.time.minute(('S', 395340)) == 6589

def test_hour():
	assert tabdil.time.hour(('d', 5)) == 120
	assert tabdil.time.hour(('H', 10)) == 10
	assert tabdil.time.hour(('m', 60)) == 1
	assert tabdil.time.hour(('S', 32400)) == 9
