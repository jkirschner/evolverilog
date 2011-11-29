"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : EvolVerilog
    Author      : Paul Booth, Shane Moon
    Date        : 11/17/11
    File Name   : Tree.py
    Description : It's a tree to be evolved!
"""
import random
from copy import deepcopy

class Tree:
    def __init__(self, numOrganismInputs, maxDepth, inputProbability,
        treeNum=0):
        self.root = Node(None, numOrganismInputs, 0, maxDepth, inputProbability)
        self.treeNum = treeNum # fix

    def __str__(self):
        return self.root.__str__()

    def count(self):
        return self.root.count()

    def crossover(self, other):
        child = deepcopy(self)
        nodeList = child.toList()
        otherNodeList = other.toList()
        childNodeIndex = random.randint(0,len(nodeList)-1)
        childNode = nodeList[childNodeIndex]
        otherNodeIndex = random.randint(0, len(otherNodeList)-1)
        otherNode = otherNodeList[otherNodeIndex]
        print "child node index: " + str(childNodeIndex)
        print "other node index: " + str(otherNodeIndex)
        #childNode = random.choice(nodeList)
        #otherNode = deepcopy(random.choice(otherNodeList))
        # we need a deepcopy because we don't want to alter original Tree
        if (childNodeIndex == 0):
            child.root = otherNode
        else:
            childNode.replaceSelf(otherNode)
        return child

    def toList(self):
        return self.root.toList()
        
    def toVerilog(self):
        return tree.root.toVerilog(self.treeNum,0)[0]
        
class Node:
    # Could include gate probabilities or weights so that buf is less likely
    # than and or xor
    gateChoices = [
            ('and',(2,2)),
            ('or',(2,2)),
            ('not',(1,1)),
            ('nand',(2,2)),
            ('xor',(2,2)),
            ('buf', (1,1))
            ]

    def __init__(self, parent, numOrganismInputs, depth, maxDepth, inputProbability):
        self.parent = parent
        self.children = []
        self.numOrganismInputs = numOrganismInputs
        self.depth = depth
        self.randomizeGate()
        self.inputProbability = inputProbability
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

    def count(self):
        count = 1
        for child in self.children:
            count += child.count()
        return count

    def toList(self):
        lst = [self]
        for child in self.children:
            lst.extend(child.toList())
        return lst

    def replaceChild(self, oldNode, newNode):
        found = False
        for i in range(len(self.children)):
            child = self.children[i]
            if (child == oldNode):
                newNode.parent = self
                self.children[i] = newNode
                found = True
        if (not found):
            raise("hell. The replaceChild is broken and couldn't find" \
                  " the old node.")

    def replaceSelf(self, newNode):
        if (self.parent):
            self.parent.replaceChild(self, newNode)
        else:
            raise "Uh oh. This shouldn't happen. You shouldn't replace root" \
                  " nodes. @ replaceSelf"

    def randomizeGate(self):
        self.gate, inputRange = random.choice(self.gateChoices)
        self.numberOfInputs = random.randint(inputRange[0], inputRange[1])

    def makeChildren(self, maxDepth):
        # Could change the inputProbability passed to children to approach 1
        # more depth , means more likely to terminate the tree
        for i in range(self.numberOfInputs):
            if (self.depth < maxDepth and random.random() > self.inputProbability):
                self.children.append(Node(self, self.numOrganismInputs,
                                          self.depth + 1, maxDepth, self.inputProbability))
            else:
                self.children.append(InputNode(self, self.numOrganismInputs,
                                          self.depth + 1, maxDepth, self.inputProbability))

    def toVerilog(self,treeNum,branchStr):
        """
        Each node needs to know the branch number of its children's
        outputs and the tree number (or id).
        
        Each node needs to know its branch number in the tree and
        the tree number (or id).
        
        Outputs: verilog,outputStr
        """
        
        verilogRes = []
        inputs = []
        for childNum, child in enumerate(self.children):
            v,output = child.toVerilog(treeNum,'%s%d'%(branchStr,childNum))
            verilogRes.append(v)
            inputs.append(output)
        
        inputStr = ','.join(inputs)
        outputStr = 'output%d_branch%s'%(treeNum,branchStr)
        verilogRes.append('\t%s #50 (%s,%s);'%(self.gate,outputStr,inputStr))
        return ('\n'.join(verilogRes),outputStr)

class InputNode(Node):

    def randomizeGate(self):
        self.inputIndex = random.randint(0, self.numOrganismInputs - 1)
        self.numberOfInputs = 0
        self.gate = "input" + str(self.inputIndex)
    
    def toVerilog(self,treeNum,branchStr):
        """
        Each node needs to know the branch number of its children's
        outputs and the tree number (or id).
        
        Each node needs to know its branch number in the tree and
        the tree number (or id).
        
        Outputs: verilog,outputStr
        """
        
        return ('\t// input comment','input%d'%self.inputIndex)
    
    #def toVerilog(self,levelName):
    #    
    #    return '%s%d_%s'%(levelName,self.depth,self.gate)

if __name__ == '__main__':
    tree = Tree(4, 3, .9)
    print "tree1"
    print tree
    print "------------------"
    tree2 = Tree(4,3,1)
    print "tree2"
    print tree2
    print "------------------"
##    print tree2.toList()
    #tree.root.replaceChild(tree.root.children[0], tree2.root)
    newtree = tree.crossover(tree2)
    print "\nnew tree"
    print newtree
    print "------------------"
    for i in range(10):
        newtree = newtree.crossover(tree)
        print i
        print newtree
##    newtree2 = tree2.crossover(tree)
##    print "new tree2"
##    print newtree2
##    print "\ntree"
##    print tree
##    print "tree2"
##    print tree2
        
    tree.root.replaceSelf(tree2.root)

    print tree
    print tree.toVerilog()
