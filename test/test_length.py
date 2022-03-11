import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_length():
	assert tabdil.length.millimeter(('km', 2)) == 2000000
	assert tabdil.length.millimeter(('m', 3)) == 3000
	assert tabdil.length.millimeter(('cm', 12)) == 120
	assert tabdil.length.millimeter(('mm', 65)) == 65
	assert tabdil.length.millimeter(('mi', 0.1)) == 160934
	
#test centimeter function
def test_centimeter():
	assert tabdil.length.centimeter(('km', 2)) == 200000
	assert tabdil.length.centimeter(('m', 3)) == 300
	assert tabdil.length.centimeter(('cm', 12)) == 12
	assert tabdil.length.centimeter(('mm', 65)) == 6.5
	assert tabdil.length.centimeter(('mi', 1)) == 160934
