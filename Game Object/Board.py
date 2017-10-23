
class Board:
	
	def __init__(self):
		pass
		

class Forest(Board):
    
    def __init__(self, height, length, forest_list):
        self.length = length
        self.height = height
        self.grid = [[Case(forest_list[i][j], i, j) for j in range(self.length)] for i in range(self.height)]
        self.link_grid()
        
    def __repr__(self):
        output = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                output += self.grid[i][j].__repr__()
            output += "\n"
        return output[:-1]
   
    def link_grid(self):
        for i in range(self.height):
            for j in range(self.length):
                case = self.grid[i][j]
                if case.letter == "*":
                    self.exit = (case.letter.i, case.letter.j)
                elif case.letter == "M":
                    self.agent = [case.letter.i, case.letter.j]
                try:
                    case.N = self.grid[i-1][j]
                    case.neighbors.append(case.N)
                except:
                    pass
                try:
                    case.S = self.grid[i+1][j]
                    case.neighbors.append(case.S)
                except:
                    pass
                try:
                    case.E = self.grid[i][j+1]
                    case.neighbors.append(case.E)
                except:
                    pass
                try:
                    case.W = self.grid[i][j-1]
                    case.neighbors.append(case.W)
                except:
                    pass
                
    def get_manhattan(self):
        return abs(self.agent[0]-self.exit[0]) + abs(self.agent[1]-self.exit[1])
        
    