class Node:
    def __init__(self, left = None, right = None, value = None):
        self.left = left
        self.right = right

Tree = Node(
    Node(
        Node(),
        Node()
    ),
    Node()
)

def prof(T):
    if T.left == None and T.right == None:
        T.prof = 1
        T.diam = 1
    else:
        T.prof = 1 + max(prof(T.left), prof(T.right))
        T.diam = 1 + T.left.prof + T.right.prof
    return T.prof

def diam(T):
    prof(T)
    return T.diam