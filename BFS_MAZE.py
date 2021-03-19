import sys
from time import sleep

class Node():
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

class QueueFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        if isinstance(state, Node) and state in self.frontier:
            return True
        else:
            return False
    
    def remove(self):
        if len(self.frontier) == 0:
            raise Exception('Frontier is empty')
    
        node = self.frontier[0]
        self.frontier.pop(0)
        return node

    def isEmpty(self):
        return len(self.frontier) == 0

class Maze():
    def __init__(self, txt):
        with open(txt, 'r') as file:
            contents = file.read()
        
        #Check if the maze is single exit/entry
        if contents.count('A') != 1 or contents.count('B') != 1:
            raise Exception('Maze must have only one entrance and exit')
        
        #Keeping track of possible paths
        self.paths = []

        #Splitting the maze in rows
        contents = contents.splitlines()
        for i in contents:
            row = []
            for j in i:
                if j == '#' or j == 'A' or j == 'B':
                    row.append(False)
                if j == 'A':
                    self.start = (i,j)
                if j == 'B':
                    self.goal = (i,j)
                else:
                    row.append(True)
            self.paths.append(row)
                   
        self.solution = None

    def print_maze():
        pass

    def solve(self):

        # Creating and Initializing frontier
        start = Node(state=self.start)
        frontier = QueueFrontier()
        frontier.add(start)

        # Creating explored set
        explored = set()
        num_explored_states = 0

        # Looping until solution is found
        while True:
            if frontier.isEmpty():
                raise Exception('No possible solution')
            
            current = frontier.remove()
            print(current)

        

if __name__ == '__main__':
    maze = Maze(sys.argv[1])
    maze.solve()