import random
import timeit
import sys
import numpy as np

sys.setrecursionlimit(10000)

try:
    from treedraw import Tree
except ImportError:
    import os
    include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, include)
    from treedraw import Tree

try:
    PY2 = sys.version_info.major is 2
except:
    PY2 = True

NUMBER = 3 if PY2 else 30
N = [10, 100, 200, 300, 500, 1000, 2000, 3000, 4000, 5000]
    # Build random trees:
T = []

def _setup(i):
    for j in range(NUMBER):
        T.append(_randomTree(N[i], 5, 10))


def _randomTree(N, minPerLevel=3, maxPerLevel=5):
    if maxPerLevel <= minPerLevel:
        raise ValueError("Expected: maxPerLevel > minPerLevel")

    # random tree with N nodes
    T = Tree("%.0f" % (random.random()*100))
    node = T.root

    counter = [1, N]

    if 1 == N:
        return T

    _randomChildren(node, minPerLevel=minPerLevel, maxPerLevel=maxPerLevel, counter=counter)

    return T

def _randomChildren(node, minPerLevel, maxPerLevel, counter):
    children = []
    for j in range(minPerLevel, random.randint(minPerLevel+1, maxPerLevel)):
        child = node.addChild("%.0f" % (random.random()*100))
        children.append(child)

        counter[0] += 1
        if counter[0] == counter[1]:
            return

    for child in children:
        _randomChildren(child, minPerLevel=minPerLevel, maxPerLevel=maxPerLevel, counter=counter)
        if counter[0] == counter[1]:
            return


def _run_speed(i):
    T.pop().walker(1.0)

def test_linear():
    times = {}
    print("Running each test %d times with random data" % NUMBER)
    for i, n in enumerate(N):
        print("n=%d nodes:" % n)
        t = timeit.timeit('test_speed._run_speed(%d)' % i, setup='import test_speed; test_speed._setup(%d)' % i, number=NUMBER)
        times[n] = t
        print("{0:25.20f}".format(t))

    x = list(times.keys())
    y = list(times.values())
    a = np.vstack([x, np.ones(len(x))]).T
    r, res, rank, s = np.linalg.lstsq(a, y)

    if res[0] < 0.01:
        print("Times seem to be O(n)")
    else:
        print("Times seem to be not linear:")
        print(r, res)

if __name__ == '__main__':
    test_linear()


