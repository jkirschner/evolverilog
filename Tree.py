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
    def __init__(self, numOrganismInputs):
        self.root = Node(None, numOrganismInputs, 0)


class Node:

    gateChoices = [
            ('and',(2,5)),
            ('or',(2,5)),
            ('not',(1,1)),
            ('buf',(1,1)),
            ('nand',(2,5)),
            ('xor',(2,5))
            ]

    def __init__(self, parent, numOrganismInputs, depth):
        self.randomizeGate()
        self.parent = parent
        self.children = []
        self.numOrganismInputs = numOrganismInputs
        self.depth = depth
        self.makeChildren()

    def randomizeGate(self):
        self.gate, inputRange = random.choice(self.gateChoices)
        self.numberOfInputs = random.randint(inputRange)

    def makeChildren(self):
        for i in range(self.numberOfInputs):
            self.children.append(Node(self))


class InputNode(Node):

    def randomizeGate(self):
        self.inputIndex = random.randint(0, self.numOrganismInputs - 1)
        
