# Styleguide

Inspired on: *Flake8 styleguide* (<https://flake8.pycqa.org/en/latest/>)

This document holds and shows all the coding and style rules we've applied within this project.

## Language and Overall style

- All comments, variable names, functions, etc. are in English
- All functions and methods contain type-hints
- All type-hints are non-capitalized (Except 'None' & 'Any')

## Comments

- Start with '#'
- After # there is a space
- Does **not** start with a (or contain) a capital letter
- Does **not** end with a period
- Does **not** has a whiteline beneath it
- Does has a whiteline above it
- comments are imperative sentences

*Example:*

```python
# this is a correct comment
```

## Naming

- Internal functions and methods are preceded with an underscore

*Example*:

```python
def _internal_function(argument):
    functionality
```

(**Definition**: Internal  functions, or methods are  meant to be used and accessed only within the confines of a specific space. They are typically not exposed to external parts of the software.)

## Doc-strings

- No newline after doc-strings
- Differences between return-values and post-condtions (=effects of the method/function)
- No capitalization at beginning of sentences
- No periods after sentences
- Doc-strings are written in third-person

*Example/template:*

```python
"""
explanation of method/function

pre: 
    pre-condition 1
    pre-condition 2

post:
    post-condition 1
    post-condition 2

returns:
    return_value 1
    return_value 2       
"""
```
