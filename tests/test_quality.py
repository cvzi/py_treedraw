import sys
try:
    from treedraw import Tree, Node
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    from treedraw import Tree, Node

def test_basic():
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

    T.walker(1.0)

    positions = [node.positionf() for node in T.nodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.positionf()[0],node.positionf()[1]) for node in T.nodes]

    assert isExpected(nodes, [('a1', 0.0, 0.0), ('b2', -1.75, 1.0), ('c5', 0.0, 1.0), ('d6', 1.75, 1.0), ('e3', -2.25, 2.0), ('f4', -1.25, 2.0), ('g7', -0.25, 2.0), ('h10', 1.25, 2.0), ('i11', 3.75, 2.0), ('j8', -0.75, 3.0), ('k9', 0.25, 3.0), ('l12', 1.25, 3.0), ('m13', 2.25, 3.0), ('n14', 3.25, 3.0), ('o15', 4.25, 3.0), ('p16', 5.25, 3.0)])

def test_int():
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

    T.walker(1.0)

    positions = [node.position() for node in T.nodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.position()[0],node.position()[1]) for node in T.nodes]

    assert isExpected(nodes, [('a1', 0, 0), ('b2', -1, 1), ('c5', 0, 1), ('d6', 2, 1), ('e3', -2, 2), ('f4', -1, 2), ('g7', 0, 2), ('h10', 2, 2), ('i11', 4, 2), ('j8', 0, 3), ('k9', 1, 3), ('l12', 2, 3), ('m13', 3, 3), ('n14', 4, 3), ('o15', 5, 3), ('p16', 6, 3)])

def test_int_scale():
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

    T.walker(1.0)

    positions = [node.position() for node in T.nodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.position(scalex=(3,2))[0],node.position(scalex=(3,2))[1]) for node in T.nodes]

    assert isExpected(nodes, [('a1', 0, 0), ('b2', -5, 2), ('c5', 0, 2), ('d6', 6, 2), ('e3', -6, 4), ('f4', -3, 4), ('g7', 0, 4), ('h10', 4, 4), ('i11', 12, 4), ('j8', -2, 6), ('k9', 1, 6), ('l12', 4, 6), ('m13', 7, 6), ('n14', 10, 6), ('o15', 13, 6), ('p16', 16, 6)])


def test_distance():
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

    T.walker(0.5)

    positions = [node.positionf() for node in T.nodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.positionf(scalex=(10.0,1.0))[0],node.positionf(scalex=(10.0,1.0))[1]) for node in T.nodes]

    assert isExpected(nodes, [('a1', 0.0, 0.0), ('b2', -8.75, 1.0), ('c5', 0.0, 1.0), ('d6', 8.75, 1.0), ('e3', -11.25, 2.0), ('f4', -6.25, 2.0), ('g7', -1.25, 2.0), ('h10', 6.25, 2.0), ('i11', 18.75, 2.0), ('j8', -3.75, 3.0), ('k9', 1.25, 3.0), ('l12', 6.25, 3.0), ('m13', 11.25, 3.0), ('n14', 16.25, 3.0), ('o15', 21.25, 3.0), ('p16', 26.25, 3.0)])

def test_remove():
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

    T.removeChild(c)
    d.removeChild(g)
    i.removeChild(n)


    T.walker(1.0)

    positions = [node.position() for node in T.nodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.position()[0],node.position()[1]) for node in T.nodes]

    assert isExpected(nodes, [('a1', 0, 0), ('b2', -1, 1), ('d6', 2, 1), ('e3', -1, 2), ('f4', 0, 2), ('h10', 1, 2), ('i11', 3, 2), ('l12', 1, 3), ('m13', 2, 3), ('o15', 3, 3), ('p16', 4, 3)])

def test_dumbtreebuilding():
    # Build a tree
    T = Tree("a1")

    b = T.addChild("b2")
    d = T.addChild("d6")

    e = b.addChild("e3")
    f = b.addChild("f4")

    h = d.addChild("h10")
    i = d.addChild("i11")

    l = h.addChild("l12")

    # Manually add children
    m = Node("m13")
    o = Node("o15")
    p = Node("p16")

    m.parent = i
    o.parent = i
    p.parent = i

    i.children = [m, o, p]

    T.walker(1.0)

    # Traverse tree to get all nodes, T.nodes is not updated
    allnodes = getNodes_preorder(T)

    positions = [node.position() for node in allnodes]

    assert noDuplicatePostions(positions)

    nodes = [(node.data,node.position()[0],node.position()[1]) for node in allnodes]

    assert isExpected(nodes, [('a1', 0, 0), ('b2', -1, 1), ('d6', 2, 1), ('e3', -1, 2), ('f4', 0, 2), ('h10', 1, 2), ('i11', 3, 2), ('l12', 1, 3), ('m13', 2, 3), ('o15', 3, 3), ('p16', 4, 3)])

def noDuplicatePostions(nodes):
    return len(set(nodes)) == len(nodes)

def isExpected(nodes, expected_nodes):
    if len(nodes) != len(expected_nodes):
        print("Length do not match")
        return False

    for node in expected_nodes:
        if node not in nodes:
            print("Expected %r was not found" % (node, ))
            return False

    return True

def getNodes_preorder(tree, nodes = []):
    node = tree if isinstance(tree, Node) else tree.root
    nodes.append(node)
    for child in node.children:
        getNodes_preorder(child, nodes)
    return nodes

def run_all():
    for fname, f in list(globals().items()):
        if fname.startswith('test_'):
            print("%s()" % fname)
            f()
            print("Ok.")


if __name__ == '__main__':
    run_all()
