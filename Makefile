SETUP_CMD=python3 setup.py
PYTEST_CMD=pytest-3


build:
	$(SETUP_CMD) build


install:
	$(SETUP_CMD) install


clean:
	rm -rf build dist tabdil.egg-info tabdil/__pycache__ test/__pycache__/


test: build
	$(PYTEST_CMD)


.PHONY: build install clean test
