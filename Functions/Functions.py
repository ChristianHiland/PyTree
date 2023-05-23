# Importing modules.
from anytree.exporter import DotExporter
from anytree import Node, RenderTree

# Vars
pre = u'\u2502'
fill = u'\u251c\u2500\u2500'
node = u'\u2570\u2500\u2500'

# Functions that are needed to make other functions work.
def nodenamefunc(node):
    return '%s:%s' % (node.name, node.depth)
def edgeattrfunc(node, child):
    return 'label="%s:%s"' % (node.name, child.name)
def edgetypefunc(node, child):
    return '--'

# The function that makes the box tree.
def DotExporterMake(rootF):
    for line in DotExporter(rootF, graph="graph",
                            nodenamefunc=nodenamefunc,
                            nodeattrfunc=lambda node: "shape=box",
                            edgeattrfunc=edgeattrfunc,
                            edgetypefunc=edgetypefunc):
        print(line)

# The function that makes the list tree.
def PrintListTree(rootF, ListFile):
    for pre, fill, node in RenderTree(rootF):
        print("%s%s" % (pre, node.name))
        with open(ListFile, "a") as List:
            List.write("%s%s" % (pre, node.name) + "\n")