# Casl
## Cool And Simple Language
## Warning: This is a work in progress. The interpreter is not usable yet!
#### What it is:
Casl is a simple programming language just made for fun. Has all the usal stuff... lexer, parser, evaluator.
#### Minimum Requirements:
As of the current version, alpha-2.0, minimum:
Python 3.0
Any functioning machine
#### File structure explained:
```interpreter.py``` is the main interpreter, which containts the lexer, parser evaluator.
It also loads in the standard library from ```standard_library_functions.json```, where all the functions are stored.
```wrapper.py``` runs everything. As of this version, the interpreter is not usable yet. But if you want to see a debug
hello world message, by all means go ahead and run ```wrapper.py``` with python!

