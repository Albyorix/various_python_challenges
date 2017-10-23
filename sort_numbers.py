

def manhatan_distance(position1, position2):
    return abs(position1[0]-position2[0]) **4 + abs(position1[1]-position2[1]) **4

class Element(object):

    def __init__(self, object):
        self.value = object

    def __repr__(self):
        rep = str(self.value)
        try:
            rep += " rank=" + str(self.rank)
        except:
            pass
        try:
            rep += " next"
            a = self.nextItem
        except:
            pass
        return rep

class Stack(object):

    def __init__(self):
        self.last = None

    def pop(self):
        if self.last == None:
            return None
        else:
            last = self.last
            self.last = self.last.previous
            return last.value

    def add(self, element):
        if self.last == None:
            self.last = element
        else:
            previous = self.last
            self.last = element
            self.last.previous = previous

class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def pop(self):
        if self.last == None:
            return None
        else:
            first = self.first
            self.first = self.first.nextItem
            return first.value

    def add(self, element):
        if self.first == None:
            self.first = element
            self.last = element
        else:
            self.last.nextItem = element
            self.last = element

class Priority_Queue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def pop(self):
        if self.last == None:
            return None
        else:
            first = self.first
            self.first = self.first.nextItem
            return first.value, first.last_move

    def add(self, element, rank):
        element.rank = rank
        element.last_move = element.value[-1]
        if self.first == None:
            self.first = element
            self.last = element
        else:
            if self.last.rank >= rank:
                self.last.nextItem = element
                self.last = element
            elif self.first.rank <= rank:
                first = self.first
                self.first = element
                self.first.nextItem = first
            else:
                self.current = self.first
                while self.current.nextItem.rank > rank:
                    self.current = self.current.nextItem
                nextItem = self.current.nextItem
                self.current.nextItem = element
                element.nextItem = nextItem


class Tree(object):

    def __init__(self, object):
        self.object = object
        self.child = {}
        self.value = self.object.heuristic()
        self.best_action = ''

    def add_child(self, link, childTree):
        self.child[link] = childTree

    def __repr__(self):
        rep = str(self.object) +"\n"
        for link in self.child.keys():
            rep += str(self.child[link].__repr__())
        return rep


class Case(object):

    def __init__(self, value, position):
        self.value = value
        self.reset_position(position)
        self.neighbor = {}

    def __repr__(self):
        return "(" + str(self.value) + ", " + str(self.position) + ")"

    def __eq__(self, other):
        return self.value == other.value

    def reset_position(self, position):
        self.position = position
        self.positionX = position[0]
        self.positionY = position[1]

    def reset_value(self, value):
        self.value = value

class Plateau(object):

    def __init__(self, matrix, static=False):
        self.dico = {}
        self.action = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.height = len(matrix)
        self.width = len(matrix[0])
        for i in range(self.height):
            if len(matrix[i]) != self.width:
                print "ERROR in the size of the matrix"
        for i in range(self.height):
            for j in range(self.width):
                self.dico[(i, j)] = Case(matrix[i][j], (i, j))
                if matrix[i][j] == 0:
                    self.void = self.dico[(i, j)]
        self.create_links()
        if not static:
            self.win_state = self.get_win_state()

    def __repr__(self):
        rep = ""
        for i in range(self.height):
            for j in range(self.width):
                rep += "|" + str(self.dico[(i, j)].value)
            rep += "|\n"
        rep = rep.replace("|0","| ")
        return rep

    def __eq__(self, other):
        if self.height == other.height and self.width == other.width:
            for key in self.dico:
                if not self.dico[key] == other.dico[key]:
                    return False
            return True
        return False

    def create_links(self):
        for i in range(self.height):
            for j in range(self.width):
                self.reset_case_links(self.dico[(i, j)])

    def get_opposite_action(self, action):
        if action == 'UP':
            return "DOWN"
        if action == "DOWN":
            return "UP"
        if action == "LEFT":
            return "RIGHT"
        if action == "RIGHT":
            return "LEFT"

    def get_matrix(self):
        L = []
        for i in range(self.height):
            L.append([])
            for j in range(self.width):
                L[i].append(self.dico[(i,j)].value)
        return L

    def deep_copy(self):
        tmpList = self.get_matrix()
        newPlateau = Plateau(tmpList)
        return newPlateau

    def get_case(self, position):
        case = self.dico[position]
        return case

    def get_position(self, case):
        for position in self.dico:
            if self.dico[position] == case:
                return position

    def get_void_position(self):
        return self.void.position

    def get_cases_and_actions(self, last_move=False):
        dico = {}
        p = self.get_void_position()
        if self.dico[p].positionX != 0:
            dico["DOWN"] = self.dico[p].neighbor["UP"]
        if self.dico[p].positionX != self.height-1:
            dico["UP"] = self.dico[p].neighbor["DOWN"]
        if self.dico[p].positionY != 0:
            dico["RIGHT"] = self.dico[p].neighbor["LEFT"]
        if self.dico[p].positionY != self.width-1:
            dico["LEFT"] = self.dico[p].neighbor["RIGHT"]
        if last_move != False:
            dico.pop(self.get_opposite_action(last_move))
        return dico

    def reset_case_links(self, case):
        i = case.positionX
        j = case.positionY
        self.dico[(i, j)].neighbor = {}
        if i != 0:
            self.dico[(i, j)].neighbor["UP"] = self.dico[(i - 1, j)]
        if i != self.height - 1:
            self.dico[(i, j)].neighbor["DOWN"] = self.dico[(i + 1, j)]
        if j != 0:
            self.dico[(i, j)].neighbor["LEFT"] = self.dico[(i, j - 1)]
        if j != self.width - 1:
            self.dico[(i, j)].neighbor["RIGHT"] = self.dico[(i, j + 1)]

    def reset_neighbors_links(self, case):
        i = case.positionX
        j = case.positionY
        try:
            self.dico[(i, j)].neighbor["UP"].neighbor["DOWN"] = self.dico[(i, j)]
        except:
            pass
        try:
            self.dico[(i, j)].neighbor["DOWN"].neighbor["UP"] = self.dico[(i, j)]
        except:
            pass
        try:
            self.dico[(i, j)].neighbor["LEFT"].neighbor["RIGHT"] = self.dico[(i, j)]
        except:
            pass
        try:
            self.dico[(i, j)].neighbor["RIGHT"].neighbor["LEFT"] = self.dico[(i, j)]
        except:
            pass

    def move_case(self, case, action):
        if not self.void == case.neighbor[action]:
            print "ERROR, the move is forbidden"
        # Switch values in the Plateau
        caseValue = case.value
        self.void.reset_value(caseValue)
        self.void.neighbor[self.get_opposite_action(action)].reset_value(0)
        self.void = case

    def move_cases(self, actions):
        for i in range(len(actions)):
            case_and_actions = self.get_cases_and_actions()
            self.move_case(case_and_actions[actions[i]], actions[i])

    def get_win_state(self):
        L = []
        for i in range(self.height):
            L.append([])
            for j in range(self.width):
                L[i].append( j + self.width * i)
        return Plateau(L, static=True)

    def heuristic(self):
        H = 0
        for case in self.dico.values():
            if case.value != 0:
                H += manhatan_distance(self.get_position(case), self.win_state.get_position(case))
        return H

class Game(object):

    def __init__(self, matrix):
        self.plateau = Plateau(matrix)
        self.turn = 0
        self.win_state = self.plateau.get_win_state()

    def is_win_state(self):
        if self.plateau.win_state == self.plateau:
            return True
        else:
            return False

    def human_play(self):
        self.last_move = None
        while self.last_move != "P" and not self.is_win_state():
            print self.plateau
            print "\nTurn: " + str(self.turn) + "\n"
            self.last_move = raw_input("What is your next move? Use the AWSD to decide or P to escape.")
            self.last_move = self.last_move.capitalize()
            self.turn += 1
            self.human_move()

        if self.last_move == 'P':
            print "Too bad, see you later"
        if self.is_win_state():
            print "Congratulation, you win"
        return

    def human_move(self):
        dico = self.plateau.get_cases_and_actions()
        if self.last_move == 'A':
            action = "LEFT"
        elif self.last_move == 'W':
            action = "UP"
        elif self.last_move == 'S':
            action ="DOWN"
        elif self.last_move == 'D':
            action = "RIGHT"
        elif self.last_move == 'P':
            return
        else:
            print "ERROR in the letter"
            return
        if action not in dico:
            print "You can't go that way"
            return
        else:
            self.plateau.move_case(dico[action], action)

    def computer_moves(self, move_list):
        for action in move_list:
            self.plateau.move_case(self.plateau.get_cases_and_actions()[action], action)
        if self.is_win_state():
            print "Congratulation, you win"

    def computer_play_without_search(self, depth = 3):
        move_list = []
        currentPlateau = self.plateau.deep_copy()
        endWhile = False
        count = 0
        best_move = False
        while not endWhile and count < 100:
            count +=1
            print currentPlateau
            if currentPlateau.heuristic() == 0:
                break
            currentSearchTree = Tree(currentPlateau)
            fill_tree(currentSearchTree, depth, best_move)
            best_move = get_best_move(currentSearchTree)
            move_list.append(best_move)
            currentPlateau.move_case( currentPlateau.get_cases_and_actions()[best_move], best_move)

        print move_list
        self.computer_moves(move_list)

    def computer_play_bfs(self):
        move_list = []
        best_move_list = []
        myQueue = Priority_Queue()
        saveDico = {}
        saveDico[self.plateau] = True
        count = 0
        currentPlateau = self.plateau.deep_copy()
        currentPlateau.move_cases(move_list)
        last_move = False
        best_rank = 99999

        while count < 2000 and currentPlateau.heuristic() != 0:
            count += 1
            case_and_actions = currentPlateau.get_cases_and_actions(last_move)

            for action, case in case_and_actions.items():
                dicoTestPlateau = currentPlateau.deep_copy()
                dicoTestPlateau.move_cases([action])
                if not dicoTestPlateau in saveDico:
                    saveDico[dicoTestPlateau] = True
                    rank = dicoTestPlateau.heuristic() + len(move_list)
                    if rank < best_rank: # Save the best_move_list so far
                        best_rank = rank
                        best_move_list = move_list
                    newList = move_list + [action]
                    element = Element( newList)
                    myQueue.add( element, -rank)

            move_list, last_move = myQueue.pop()
            currentPlateau = self.plateau.deep_copy()
            currentPlateau.move_cases(move_list)
        print "Move = ", count
        self.computer_moves(best_move_list)

    def computer_play_multiple_bfs(self):
        count = 0
        while count < 10 and self.plateau.heuristic() != 0:
            count += 1
            self.computer_play_bfs()
            print self.plateau.heuristic()


def fill_tree(currentSearchTree, depth = 2, last_move=False):
    if depth <= 0:
        return
    currentPlateau = currentSearchTree.object
    cases_and_actions = currentPlateau.get_cases_and_actions(last_move)

    for action, case in cases_and_actions.items():
        newPlateau = currentPlateau.deep_copy()
        newPlateau.move_case(case, action)
        newSearchTree = Tree(newPlateau)
        currentSearchTree.add_child(action, newSearchTree)
        if depth > 1:
            fill_tree(newSearchTree, depth-1, action)

def get_best_move(currentSearchTree):
    best_heuristic = 99999
    for action, newTree in currentSearchTree.child.items():
        if newTree.child != {}:
            get_best_move(newTree)


        if newTree.value < best_heuristic: # if its better
            currentSearchTree.best_action = action
            if currentSearchTree.value > newTree.value:
                currentSearchTree.value = newTree.value
            best_heuristic = newTree.value
        del currentSearchTree.child[action]
    return currentSearchTree.best_action


if __name__ == "__main__":

    a = [[1,4,2],
         [3,0,5],
         [6,7,8]]

    b = [[8,0,2],
         [7,4,6],
         [5,1,3]]

    c = [[8, 0, 2, 9],
         [7, 4, 6, 10],
         [5, 1, 3, 11],
         [15, 13, 14, 12]]


    board = Game(c)
    #board.human_play()
    #board.computer_play_without_search()
    #board.computer_play_bfs()
    board.computer_play_multiple_bfs()


