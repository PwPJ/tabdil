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
