import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_weight():
	assert tabdil.weight.milli_gram(('ton', 3)) == 3000000000
	assert tabdil.weight.milli_gram(('kg', 13)) == 13000000
	assert tabdil.weight.milli_gram(('g', 26)) == 26000
	assert tabdil.weight.milli_gram(('mg', 70)) == 70
