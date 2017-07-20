treedraw.py
===========

![Example screenshot with pygame](https://raw.githubusercontent.com/cvzi/py_treedraw/master/pygame_treedraw_example.png)

This module implements a layout algorithm for a tree.
Each node in the tree has a layout property that contains an x and y 
coordinate.
The layout is calculated by calling the method "walker(distance)".
The distance property indicated the distance between nodes on the same level.
If the tree is build up using the addChild/removeChild methods, the layout
will be calculated in linear time. 
The algoithm is a python implemenation of this publication ["Improving 
Walker's Algorithm to Run in Linear Time"](http://citeseer.ist.psu.edu/buchheim02improving.html) by Christoph Buchheim, Michael Jünger, Sebastian Leipert


Tested with Python 2.6 and 3.4


The example/__main__ requires pygame for the graphical interface
