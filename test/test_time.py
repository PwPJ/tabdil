import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_seconds():
	assert tabdil.time.seconds(('d', 5)) == 432000
	assert tabdil.time.seconds(('H', 10)) == 36000
	assert tabdil.time.seconds(('m', 13)) == 780
	assert tabdil.time.seconds(('S', 987654321)) == 987654321
