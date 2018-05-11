class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def createNode(parent,i,created,root):
    # print(i)
    if created[i] is not None:
        return
    created[i] = Node(i)

    if parent[i]==-1:
        root[0]=created[i]
        return

    if created[parent[i]] is None:
        createNode(parent,parent[i],created,root)

    p = created[parent[i]]

    if p.left is None:
        p.left = created[i]
    else:
        p.right=created[i]


def createTree(parent):
    n = len(parent)

    created=[None for i in range(n+1)]
    root=[None]

    for i in range(n):
        # print(i)
        createNode(parent,i,created,root)

    return root[0]


def preorder(root):
    if root is not None:
        print(root.key)
        preorder(root.left)
        preorder(root.right)

def deletenode(root,todel):
    if root is not None:
        if root.key==todel:
            root.left=None
            root.right=None
            root.key=None
        else:
            deletenode(root.left, todel)
            deletenode(root.right, todel)
        return root


def countleaves(root):
    count=0
    if root.key != None:
        if root.left is None and root.right is None:
            count=count+1
        if root.left:
            count += countleaves(root.left)
        if root.right:
            count+=countleaves(root.right)
    return count



N = input()
parent_str=input()
todelete=int(input())

parent_temp = parent_str.split(" ")
parent = [int(x) for x in parent_temp]

root = createTree(parent)
newroot=deletenode(root,todelete)
count = countleaves(newroot)
# preorder(newroot)
print(count)
