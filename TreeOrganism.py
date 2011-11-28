"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/24/2011
    File Name   : Tree.py
    Description :
"""

import random
import testOrgs
import Organism
import Tree

class TreeOrganism(Organism):
    
    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, maxDepth=4, moduleName='organism'):
        """
            Assumption: numOutputs = numTrees
        """
        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.moduleName = moduleName
        self.fitness = None
        self.trees = [None]*numOutputs
        self.maxDepth = maxDepth
        if randomInit:
            self.randomInitialize()
        
    def __str__(self):
        contents = '\n Tree: '.join(str(tree) for tree in self.trees)
        return 'Trees: [\n %s ]\n' % contents

    def randomInitialize(self):
        """
            Return Type: void
        """
        for tree in range(self.numOutputs):
            self.trees[tree] = Tree(numOrganismInputs = self.numInputs,
                                    maxDepth = self.maxDepth)
    
    def crossover(self, otherOrganism):
        """
            Return Type: <TreeOrganism>
            Crossovers self with another <TreeOrganism>, and returns a new
            <TreeOrganism>.
        """
        # Needs to be implemented #
        print "TreeOrganism->Crossover needs to be implemented."
        return

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
