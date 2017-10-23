
class Agent:

	def __init__(board=Board, waiting_line=WaitingLine, search_algo=SearchAlgo):
		pass
	
  
class MyAgent(Agent):
    
    def __init__(self, forest):
        self.i = forest.agent.i
        self.j = forest.agent.j
        self.forest = forest
        
    def move(self, direction):
        if direction == "N":
            pass
        
        