from anytree import Node
from anytree.exporter import DotExporter
from Functions import *
from os import system, path

ListFile = "Output/List.txt"

# Root
rootF = Node("Root '/'")
# Folders under Root.
bin = Node("/bin", parent=rootF)
boot = Node("/boot", parent=rootF)
dev = Node("/dev", parent=rootF)
etc = Node("/etc", parent=rootF)
home = Node("/home", parent=rootF)
lib = Node("/lib", parent=rootF)
media = Node("/media", parent=rootF)
mnt = Node("/mnt", parent=rootF)
opt = Node("/opt", parent=rootF)
sbin = Node("/sbin", parent=rootF)
srv = Node("/srv", parent=rootF)
tmp = Node("/tmp", parent=rootF)
usr = Node("/usr", parent=rootF)
var = Node("/var", parent=rootF)
rootUF = Node("/root", parent=rootF)
proc = Node("/proc", parent=rootF)
# Folders under home.
user = Node("/user", parent=home)
# Folders under usr.
local = Node("/local", parent=usr)
# Folders under local.
bin2 = Node("/bin/", parent=local)
games = Node("/games", parent=local)
#Folders under lib.
apt = Node("/apt", parent=lib)
dpkg = Node("/dpkg", parent=lib)
gcc = Node("/gcc", parent=lib)
Python3 = Node("/python3", parent=lib)
Python27 = Node("/pytho2.7", parent=lib)
openssh = Node("/openssh", parent=lib)
dropbear = Node("/dropbear", parent=lib)
lsb = Node("/lsb", parent=lib)
init = Node("/init", parent=lib)
mime = Node("/mime", parent=lib)

# Printing the list
print("This is what the Linux Filesystem looks like.\n")
# Printing the tree list.
if path.isfile(ListFile) == False:
    system("./First.sh")
PrintListTree(rootF, ListFile)
# Printing, and making a box tree.
DotExporter(rootF).to_dotfile("tree.dot")
system("./MakePNG.sh")