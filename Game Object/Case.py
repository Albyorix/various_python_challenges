class Case:

    def __init__(self, container, neighbors=[])
        self.container = container
        self.neighbors = []
        
    def __repr__(self):
        return self.letter
    
    def position(self):
        return str((i,j))
    
    def is_tree(self):
        if self.letter == "X":
            return True
        return False

class GameCase(Case):
    
    def __init__(self, letter, i, j):
        self.letter = letter
        self.i = i
        self.j = j
        self.N = None
        self.S = None
        self.E = None
        self.W = None
        
      
        
size = L[1].split(' ')
forest = Forest( int(size[0]), int(size[1]), L[2:2+int(size[0])])
print forest