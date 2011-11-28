"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/24/2011
    File Name   : TreeOrganism.py    
    Description :
"""

import random
import Tree
from Organism import Organism
import testOrgs
import Tree

class TreeOrganism(Organism):

    treeCrossOverProbability = .7

    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, maxDepth=10, inputProbability = .2, moduleName='organism'):
        # inputProbability should be reconsidered, and not just passed in
        # We should develop a way to decide what this value should be

        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.moduleName = moduleName
        self.fitness = None
        self.maxDepth = maxDepth
        self.inputProbability = inputProbability
        self.trees = []        
        
        if randomInit:
            self.randomInitialize()
            
    def __str__(self):
        contents = '\n'.join(str(tree) for tree in self.trees)
        return 'TreeOrganism: {\n%s, fitness: %s}'%(contents, str(self.fitness))
        

    def randomInitialize(self):
        """
            Return Type: void
        """
        for i in range(self.numOutputs):
            self.trees.append(Tree(self.numInputs, self.maxDepth,
                                   self.inputProbability))
    
    def crossover(self, otherOrganism):
        """
            Return Type: <TreeOrganism>
            Crossovers self with another <TreeOrganism>, and returns a new
            <TreeOrganism>.
        """
        result = TreeOrganism(self.verilogFilePath, self.numInputs,#change verilogFilePath??
                              self.numOutputs, False, self.maxDepth,
                              self.inputProbability, self.moduleName)
        for i in range(self.numOutputs):
            selfTree = self.trees[i]
            otherTree = otherParent.trees[i]
            if (random.random() > treeCrossOverProbability):
                if (random.random() < .5):
                    result.trees.append(selfTree)
                else:
                    result.trees.append(otherTree)
            else:
                if (random.random() < .5):
                    result.trees.append(selfTree.crossover(otherTree))
                else:
                    result.trees.append(otherTree.crossover(selfTree))

        return result

    def mutate(self):
        """
            Mutates stuff
            Return Type: <TreeOrganism>
        """
        # Needs to be implemented #
        print "TreeOrganism->mutate needs to be implemented."
        return
    
    def toVerilog(self, filepath, moduleName):
        """
            Writes Organism to a verilog file.
        """
        # Needs to be implemented #
        print "TreeOrganism->toVerilog needs to be implemented."

    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        """
            Return Type: float
        """
        # Needs to be implemented #
        print "TreeOrganism->fitnessFunction needs to be implemented."
        score = 0.0
        return score
        
    def getTrees(self):
        return self.trees
    
    def replaceTree(self, tree, index):
        self.trees[index] = tree
        
if __name__ == '__main__':
    #testOrganism = BooleanLogicOrganism('TestCode/andTest.v',2,1,randomInit=True,moduleName='andTest')
    #print testOrganism
    
    #defaultResult = testOrgs.testOrganism('TestCode/andTest.v', '.', 2, 1, 'andTest',clearFiles=True)
    #simMap = testOrgs.SimulationMap(defaultResult)
    
    #print testOrganism.evaluate(simMap)
    
    defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 4, 'fourBool',clearFiles=True)
    simMap = testOrgs.SimulationMap(defaultResult)
    
    a = TreeOrganism('fourBool.v',4,4,randomInit=True,moduleName='fourBool')
    b = a.evaluate(simMap)
    print a
    print b
    #testOrganism = BooleanLogicOrganism('',4,4,randomInit=True,moduleName='')
    #testOrganism.toVerilog('organismToVerilogTest.v','test')  
