import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil


def test_mili_gram():
	assert tabdil.weight.milli_gram(('ton', 3)) == 3000000000
	assert tabdil.weight.milli_gram(('kg', 13)) == 13000000
	assert tabdil.weight.milli_gram(('g', 26)) == 26000
	assert tabdil.weight.milli_gram(('mg', 70)) == 70
	assert tabdil.weight.milli_gram(('po', 1)) == 453592

def test_gram():
    assert tabdil.weight.gram(('ton',2)) == 2000000
    assert tabdil.weight.gram(('kg',2))  == 2000
    assert tabdil.weight.gram(('g',2))   == 2
    assert tabdil.weight.gram(('mg',2))  == 0.002
    assert tabdil.weight.gram(('mg',2000)) == 2
    assert tabdil.weight.gram(('po', 200000)) == 90718474
