import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_temp():
	assert tabdil.temperature.celsius(('k', 4)) == 277.15
	assert tabdil.temperature.celsius(('f', 48)) == 488
