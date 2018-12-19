# Small example
from treedraw import Tree

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

# Draw the tree (requires pygame)
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
