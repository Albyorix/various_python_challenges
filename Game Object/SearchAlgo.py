

class SearchAlgo:
	
	def __init__(self):
		pass
 
	def run(self):
		print "Not defined"
		
	
class BFS(SearchAlgo):
    
	def __init__(self):
		pass
    
    def run(self):
		pass

		
class DFS(Agent):
    
	def __init__(self):
		pass

    def run(self, queue=None):
        if queue is None:
            queue = []
        for neighbor in self.forest.grid[self.i][self.j]:
            
       