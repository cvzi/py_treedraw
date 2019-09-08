treedraw.py
===========

![Example screenshot with pygame](https://raw.githubusercontent.com/cvzi/py_treedraw/master/pygame_treedraw_example.png)

This module implements a layout algorithm for a tree.
Each node in the tree has a layout property that contains an x and y 
coordinate.

The layout is calculated by calling the method "walker(distance)".

The distance property indicated the distance between nodes on the same level.
If the tree is build up using the addChild/removeChild methods, the layout
will be calculated in linear time _O(n)_. 

The algorithm is a python implemenation of this publication ["Improving 
Walker's Algorithm to Run in Linear Time"](http://citeseer.ist.psu.edu/buchheim02improving.html) by Christoph Buchheim, Michael Jünger, Sebastian Leipert.

Tested with Python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6 and 3.7

The example code ([example.py](https://github.com/cvzi/py_treedraw/blob/master/example.py#L37-L92)) requires [pygame](https://www.pygame.org/wiki/GettingStarted) for the graphical interface.

[![Build Status](https://travis-ci.org/cvzi/py_treedraw.svg?branch=master)](https://travis-ci.org/cvzi/py_treedraw)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5324af341edb4e17b7ef69c78b3078ed)](https://www.codacy.com/app/cuzi/py_treedraw?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cvzi/py_treedraw&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/cvzi/py_treedraw/badge.svg?branch=master)](https://coveralls.io/github/cvzi/py_treedraw?branch=master)
