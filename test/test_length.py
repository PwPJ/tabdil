import pytest
import sys
from os import getcwd

# Add module path to python's search path:
sys.path.append(getcwd())


import tabdil

#test millimeter function
def test_length():
	assert tabdil.length.millimeter(('km', 2)) == 2000000
	assert tabdil.length.millimeter(('m', 3)) == 3000
	assert tabdil.length.millimeter(('cm', 12)) == 120
	assert tabdil.length.millimeter(('mm', 65)) == 65
	assert tabdil.length.millimeter(('inch', 47)) == 1193.8
	
#test centimeter function
def test_centimeter():
	assert tabdil.length.centimeter(('km', 2)) == 200000
	assert tabdil.length.centimeter(('m', 3)) == 300
	assert tabdil.length.centimeter(('cm', 12)) == 12
	assert tabdil.length.centimeter(('mm', 65)) == 6.5	
	assert tabdil.length.centimeter(('inch', 32)) == 81.28

#test meter function
def test_meter():
	assert tabdil.length.meter(('km', 5)) == 5000
	assert tabdil.length.meter(('m', 6)) == 6
	assert tabdil.length.meter(('cm', 600)) == 6
	assert tabdil.length.meter(('mm', 450)) == 0.45	
	assert tabdil.length.meter(('inch', 35)) == 0.889

#test kilometer function
def test_kilometer():
	assert tabdil.length.kilometer(('km', 5)) == 5
	assert tabdil.length.kilometer(('m', 6)) == 0.006
	assert tabdil.length.kilometer(('cm', 600)) == 0.006
	assert tabdil.length.kilometer(('mm', 45000)) == 0.045	
	assert tabdil.length.kilometer(('inch', 35)) == 0.000889
 
#test inch function
def test_inch():
	assert tabdil.length.inch(('km', 5)) == 196850
	assert tabdil.length.inch(('m', 10)) == 393.7
	assert tabdil.length.inch(('cm', 4)) == 1.5748
	assert tabdil.length.inch(('mm', 2)) == 0.07874	
	assert tabdil.length.inch(('inch', 35)) == 35
 
