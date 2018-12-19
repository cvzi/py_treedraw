"""
treedraw.py
===========

https://github.com/cvzi/py_treedraw

Tested with Python 2.6 and 3.4

This module implements a layout algorithm for a tree.
Each node in the tree has a layout property that contains an x and y
coordinate.
The layout is calculated by calling the method "walker(distance)".
The distance property indicated the distance between nodes on the same level.
If the tree is build up using the addChild/removeChild methods, the layout
will be calculated in linear time.
The algoithm is a python implemenation of this publication
<a href="http://citeseer.ist.psu.edu/buchheim02improving.html"> "Improving
Walker's Algorithm to Run in Linear Time"</a> by Christoph Buchheim, Michael
Junger, Sebastian Leipert"
"""

__all__ = ["Tree", "Node"]

__version__ = "1.4"

import math

try:
    xrange(5)
    myrange = xrange
except NameError:
    myrange = range


class Tree:

    def __init__(self, data):
        # Start a tree with a root node
        self.root = Node(data)
        self.root.tree = self
        self.root.leftSibling = None
        self.nodes = [self.root]

    def addNode(self, node):
        # add a child to the root
        return self.root.addNode(node)

    def addChild(self, data):
        # add a child to the root
        return self.root.addChild(data)

    def walker(self, distance=1.0):
        # Init layout algorithm
        self._firstWalk(self.root, distance)
        self._secondWalk(self.root, -self.root.layout.prelim)

    def _add(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        return node

    def _firstWalk(self, v, distance):
        if v.children:
            defaultAncestor = v.children[0]
            for w in v.children:
                self._firstWalk(w, distance)
                self._apportion(w, defaultAncestor, distance)
            self._executeShifts(v)
            midpoint = 0.5 * \
                (v.children[0].layout.prelim + v.children[-1].layout.prelim)
            w = self._leftSibling(v)
            if w is not None:
                v.layout.prelim = w.layout.prelim + distance
                v.layout.mod = v.layout.prelim - midpoint
            else:
                v.layout.prelim = midpoint
        else:
            ls = self._leftSibling(v)
            if ls:
                v.layout.prelim = ls.layout.prelim + distance

    def _secondWalk(self, v, m):
        v.layout.x(v.layout.prelim + m)
        for w in v.children:
            self._secondWalk(w, m + v.layout.mod)

    def _apportion(self, v, defaultAncestor, distance):
        w = self._leftSibling(v)
        if w is not None:
            v_p_o = v
            v_p_i = v
            v_m_i = w
            v_m_o = v_p_i.parent.children[0]
            s_p_i = v_p_i.layout.mod
            s_p_o = v_p_o.layout.mod
            s_m_i = v_m_i.layout.mod
            s_m_o = v_m_o.layout.mod
            while v_m_i.nextRight() and v_p_i.nextLeft():
                v_m_i = v_m_i.nextRight()
                v_p_i = v_p_i.nextLeft()
                v_m_o = v_m_o.nextLeft()
                v_p_o = v_p_o.nextRight()
                v_p_o.layout.ancestor = v
                shift = v_m_i.layout.prelim + s_m_i - \
                    (v_p_i.layout.prelim + s_p_i) + distance
                if shift > 0:
                    self._moveSubtree(
                        self._ancestor(
                            v_m_i, v, defaultAncestor), v, shift)
                    s_p_i = s_p_i + shift
                    s_p_o = s_p_o + shift
                s_m_i = s_m_i + v_m_i.layout.mod
                s_p_i = s_p_i + v_p_i.layout.mod
                s_m_o = s_m_o + v_m_o.layout.mod
                s_p_o = s_p_o + v_p_o.layout.mod
            if v_m_i.nextRight() and v_p_o.nextRight() is None:
                v_p_o.layout.thread = v_m_i.nextRight()
                v_p_o.layout.mod = v_p_o.layout.mod + s_m_i - s_p_o
            if v_p_i.nextLeft() and v_m_o.nextLeft() is None:
                v_m_o.layout.thread = v_p_i.nextLeft()
                v_m_o.layout.mod = v_m_o.layout.mod + s_p_i - s_m_o
                defaultAncestor = v
        return defaultAncestor

    @staticmethod
    def _leftSibling(v):
        if v.leftSibling != -1:
            return v.leftSibling
        else:
            if v.parent is None or not v.parent.children:
                return None
            last = None
            for w in v.parent.children:
                if w == v:
                    if last is not None:
                        return last
                    return None
                last = w
            return None

    def _moveSubtree(self, w_m, w_p, shift):
        subtrees = w_p.number() - w_m.number()
        w_p.layout.change = w_p.layout.change - shift / subtrees
        w_p.layout.shift = w_p.layout.shift + shift
        w_m.layout.change = w_m.layout.change + shift / subtrees
        w_p.layout.prelim = w_p.layout.prelim + shift
        w_p.layout.mod = w_p.layout.mod + shift

    @staticmethod
    def _executeShifts(v):
        shift = 0
        change = 0
        i = len(v.children)
        for i in myrange(len(v.children) - 1, -1, -1):
            w = v.children[i]
            w.layout.prelim = w.layout.prelim + shift
            w.layout.mod = w.layout.mod + shift
            change = change + w.layout.change
            shift = shift + w.layout.shift + change

    @staticmethod
    def _ancestor(v_i, v, defaultAncestor):
        if v_i.layout.ancestor.parent == v.parent:
            return v_i.layout.ancestor
        return defaultAncestor


class Node:

    class Layout:
        def __init__(self, v):
            self.node = v
            self.mod = 0
            self.thread = None
            self.ancestor = v
            self.prelim = 0
            self.shift = 0
            self.change = 0
            self.pos = [None, None]
            self.number = -1  # undefined

        def x(self, value=None):
            if value is not None:
                self.pos[0] = value
            else:
                return self.pos[0]

        def y(self, value=None):
            if value is not None:
                self.pos[1] = value
            else:
                if self.pos[1] is None:
                    self.pos[1] = self.node.level()
                return self.pos[1]

    def __init__(self, data):
        self.tree = None
        self.data = data
        self.leftSibling = -1  # undefined, outdated
        self.children = []
        self.parent = None
        self.layout = self.Layout(self)

    def addNode(self, node):
        # Add an existing tree/node as a child

        # Set left sibling
        if self.children:
            node.leftSibling = self.children[-1]
            node.layout.number = node.leftSibling.layout.number + 1
        else:
            node.leftSibling = None
            node.layout.number = 0

        # Append to node
        node.parent = self
        self.children.append(node)

        # Add to tree
        root = self
        i = 0
        while root.parent is not None:
            root = root.parent
            i += 1
        root.tree._add(node)
        node.tree = root.tree
        self.layout.pos[1] = i  # Level
        return node

    def addChild(self, data):
        # Create a new node and add it as a child
        return self.addNode(Node(data))

    def removeChild(self, v):
        j = -1
        for i in myrange(len(self.children)):
            if self.children[i] == v:
                del self.children[i]
                j = 1
        for i in myrange(len(self.tree.nodes)):
            if self.tree.nodes[i] == v:
                del self.tree.nodes[i]
        # Update left sibling
        if j == 0:
            self.children[0].leftSibling = None
        elif j > 0:
            self.children[j].leftSibling = self.children[j - 1]
        # Update numbers
        for i in myrange(j, len(self.children)):
            self.children[i] = i

    def nextLeft(self):
        if self.children:
            return self.children[0]
        else:
            return self.layout.thread

    def nextRight(self):
        if self.children:
            return self.children[-1]
        else:
            return self.layout.thread

    def level(self):
        if self.layout.pos[1] is not None:
            return self.layout.pos[1]
        n = self.parent
        i = 0
        while n is not None:
            n = n.parent
            i += 1
        return i

    def position(self, origin=(0, 0), scalex=1.0, scaley=None):
        """ Return position as integer
         Examples:
         position(origin)
         position(origin, 10)
         position(origin, 10, 15)
         position(origin, (10, 15))"""
        if scaley is None:
            if hasattr(scalex, "__getitem__"):
                scalex = scalex[0]
                scaley = scalex[1]
            else:
                scaley = scalex
        return (origin[0] + int(math.ceil(self.layout.x() * scalex)),
                origin[1] + int(math.ceil(self.layout.y() * scaley)))

    def positionf(self, origin=(0.0, 0.0), scalex=1.0, scaley=None):
        """ Return position as floating point
         Examples:
         position(origin)
         position(origin, 10)
         position(origin, 10, 15)
         position(origin, (10, 15))"""
        if scaley is None:
            if hasattr(scalex, "__getitem__"):
                scalex = scalex[0]
                scaley = scalex[1]
            else:
                scaley = scalex
        return (origin[0] + (self.layout.x() * scalex),
                origin[1] + (self.layout.y() * scaley))

    def number(self):
        if self.layout.number != -1:
            return self.layout.number
        else:
            if self.parent is None:
                return 0
            else:
                i = 0
                for node in self.parent.children:
                    if node == self:
                        return i
                    i += 1
            raise Exception("Error in number(self)!")


if __name__ == '__main__':
    # Small test (with pygame)

    # Build a tree
    T = Tree("a1")

    b = T.addChild("b2")
    c = T.addChild("c5")
    d = T.addChild("d6")

    e = b.addChild("e3")
    f = b.addChild("f4")

    g = d.addChild("g7")
    h = d.addChild("h10")
    i = d.addChild("i11")

    j = g.addChild("j8")
    k = g.addChild("k9")

    l = h.addChild("l12")

    m = i.addChild("m13")
    n = i.addChild("n14")
    o = i.addChild("o15")
    p = i.addChild("p16")

    # Calculate layout
    T.walker(0.6)

    # Print coordinates
    print("Node:\t    x,\ty")
    for node in T.nodes:
        p = node.position(origin=(0, 0), scalex=100, scaley=1)
        print("%s:\t(%#4d,\t%d)" % (node.data, p[0], p[1]))

    # Draw the tree
    import pygame
    import pygame.gfxdraw
    import sys
    import time

    width, height = 800, 400
    sizex, sizey = 130, 60
    rootpos = (width / 2 - 100, height / 2 - 100)

    # Create the screen
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('tree drawing with pygame')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))

    # Draw edges
    for node in T.nodes:
        if node.parent:
            pygame.draw.aaline(
                screen, (0, 0, 0), node.position(
                    rootpos, sizex, sizey), node.parent.position(
                    rootpos, sizex, sizey))

    # Draw vertices
    for node in T.nodes:

        myfont = pygame.font.Font(None, 36)
        label = myfont.render(node.data, 1, (0, 0, 0))
        textrect = label.get_rect()
        textrect.centerx = node.position(rootpos, sizex, sizey)[0]
        textrect.centery = node.position(rootpos, sizex, sizey)[1]

        p = textrect.copy().inflate(10, 10)
        pygame.draw.ellipse(screen, (255, 255, 255), p)
        pygame.gfxdraw.aaellipse(screen, p.centerx, p.centery, int(
            p.width / 2), int(p.height / 2), (0, 255, 255))

        screen.blit(label, textrect)

    # Show everything
    pygame.display.flip()

    # Stop on q, Escape or "Close Window" button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and (
                    event.unicode == '\x1b' or event.unicode == 'q')):
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        time.sleep(0.1)
