# Styleguide

Inspired on: *Flake8 styleguide* (<https://flake8.pycqa.org/en/latest/>)

This document holds and shows all the coding and style rules we've applied within this project.

## Language and Overall style

- All comments, variable names, functions, etc. are in English
- All functions and methods contain type-hints
- All type-hints are non-capitalized (Except 'None' & 'Any')

## Comments

- start with '#'
- after # there is a space
- does **not** start with a (or contain) a capital letter
- does **not** end with a period

*Example:*

```python

# this is a correct comment
```

## Doc-strings

*Example/template:*

```python

"""
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
