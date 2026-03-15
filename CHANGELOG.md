# Version: alpha-2.0 (Misty Mountains)

### Features:
Created basic parsing capabilities.

### Changes:
Slightly changed the ast structure to include the datatype of arguments.
Changed the standard library configuration so that it only holds the required datatype of arguments, excluding the name.
**Changes to the print function**
Slighly adjusted the code to accomodate the changed ast structure
Slightly adjusted the code to accomodate the changed standard library configuration
Adjusted the code in a way so it only accepts a single argument
### Bug fixes:
None.
### Known issues:
The parser's argument output is unclean, leaving whitespaces and quotes
The parser does not include datatype as its input into the ast, leaving `None` as a placeholder
The interpreter either crashes or ignores within disovering an error, due to the lack of error handling.
### Dev note:
this project is half-fun half-pissing me off (even more so when i do error handling)
im not fixing the known issues in this release theyll be fixed in alpha-2.5, the error handling update
the final part of this update worked first try im scared

#### Version numbering explained:
Starts with alpha:
```alpha-1.0```
Alpha is when the interpreter is in a non usable state.
Every major alpha version is a +1.
Every hotfix/minor alpha version is a +0.5
When the alpha version reaches 3.0, it switches to beta.
Starts with beta:
```beta-1.0```
Beta is when the interpreter is in a barely usable state.
Every major beta version is a +1.
Every hotfix/minor beta version is a +0.5
When the beta version reaches 3.0, it switches to release.
Starts with release:
```release-1.0```
Release is when the interpreter is in a usable, turing-complete state.
Every major release version is a +0.1.
Every hotfix/minor beta version is a +0.02


