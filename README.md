# Tabdil

Tabdil is a Python program that provides you with the possibility of converting measure.

## Prerequisites

Install setuptools befor run setup.py

```bash
pip3 install setuptools
```

## Installation

you can refer to makefile and use bellow commands for install and clean project :

### Install

```bash
python3 setup.py install
```

### Clean

```bash
rm -rf  build dist tabdil.egg-info tabdil/__pycache__ test/__pycache__/
```

## Usage

```python
.../tabdil$ python3
>>> import tabdil
>>> tabdil.time.seconds(('d',5))
432000
>>> tabdil.length.millimeter(('m',2))
2000
>>> tabdil.weight.milli_gram(('ton',2))
2000000000
>>> tabdil.weight.gram(('kg',3))
3000
>>> 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgements

Whenever you need to use this program, just import it.

```bash
import tabdil
```

## License

[Creativecommons](https://creativecommons.org/licenses/by/2.0/)
