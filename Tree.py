"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : EvolVerilog
    Author      : Paul Booth, Shane Moon
    Date        : 11/17/11
    File Name   : Tree.py
    Description : It's a tree to be evolved!
"""
import random
class Tree:
    def __init__(self, numOrganismInputs, maxDepth):
        self.root = Node(None, numOrganismInputs, 0, maxDepth)


    def __str__(self):
        return self.root.__str__()
    
class Node:

    gateChoices = [
            ('and',(2,2)),
            ('or',(2,2)),
            ('not',(1,1)),
            ('nand',(2,2)),
            ('xor',(2,2)),
            ('buf', (1,1))
            ]

    def __init__(self, parent, numOrganismInputs, depth, maxDepth):
        self.parent = parent
        self.children = []
        self.numOrganismInputs = numOrganismInputs
        self.depth = depth
        self.randomizeGate()
        self.makeChildren(maxDepth)

    def __str__(self):
        s = self.gate + "[" + str(self.numberOfInputs) + "]("
        for child in self.children:
            s +=  child.__str__() + ","

        if (len(self.children) > 0):
            s = s[0:-1] + ")"
        else:
            s += ")"
        return s

    def randomizeGate(self):
        self.gate, inputRange = random.choice(self.gateChoices)
<<<<<<< HEAD
        self.numberOfInputs = random.randint(inputRange[0], inputRange[1])
=======
        self.numberOfInputs = random.randint(*inputRange)
>>>>>>> b08d98e338f71fc27de302fc957ceff0ad62ad57

    def makeChildren(self, maxDepth):
        for i in range(self.numberOfInputs):
<<<<<<< HEAD
            if (self.depth < maxDepth and random.randint(0,9) < 9):
                self.children.append(Node(self, self.numOrganismInputs,
                                          self.depth + 1, maxDepth))
            else:
                self.children.append(InputNode(self, self.numOrganismInputs,
                                          self.depth + 1, maxDepth))
=======
            if (random.randint(0,9) < 9):
                self.children.append(Node(self))
            else:
                self.children.append(InputNode(self))
>>>>>>> b08d98e338f71fc27de302fc957ceff0ad62ad57

class InputNode(Node):

    def randomizeGate(self):
        self.inputIndex = random.randint(0, self.numOrganismInputs - 1)
        self.numberOfInputs = 0
<<<<<<< HEAD
        self.gate = "input" + str(self.inputIndex)
        

if __name__ == '__main__':
    tree = Tree(4, 3)
    print tree
=======
        self.gate = 'input'

if __name__ == '__main__':
    Tree(3)
>>>>>>> b08d98e338f71fc27de302fc957ceff0ad62ad57
