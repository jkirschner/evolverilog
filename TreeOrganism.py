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
from Organism import *
from Tree import *

def verilogFromTemplate(moduleName,moduleArgs,moduleBody):

    template = """module %s(%s);\n\n%s\n\nendmodule"""
    
    return template%(moduleName,moduleArgs,moduleBody)

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

    def randomInitialize(self):
        """
            Return Type: void
        """
        for tree in range(self.numOutputs):
            self.trees[tree] = Tree(numOrganismInputs = self.numInputs,
                                    maxDepth = self.maxDepth)
    
    def crossover(self, otherOrganism):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
        """
        return NotImplementedError, 'Crossover method from Organism must be overwritten.'        
        
    def __str__(self):
        contents = '\n Tree: '.join(str(tree) for tree in self.trees)
        return 'Trees: [\n %s ]\n' % contents

    def toVerilog(self, filepath, moduleName):
        """
            Writes Organism to a verilog file.
        """

        # Needs to be implemented #
        print "I should be implemented!!!!"

    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        """
            Return Type: float
            NEEDS TO BE IMPLEMENTED
        """
        score = 0.0
        return score
        
    def getTrees(self):
        return self.trees
    
    def replaceTree(self, tree, index):
        self.trees[index] = tree

class BooleanLogicOrganism(Organism):
    
       
    def crossover(self, otherParent):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
            Assumes both gates have the same # of layers, etc.
        """
        result = BooleanLogicOrganism(self.verilogFilePath, self.numInputs, self.numOutputs,  #change verilogFilePath??
            False, self.nLayers, self.nGates, self.moduleName)

        selfLayers = self.getLayers()
        otherLayers = otherParent.getLayers()
        for index in range(len(selfLayers)):
            newLayer = selfLayers[index].crossover(otherLayers[index])
            # print selfLayers[index], "\nLAYER crossing over with\n", otherLayers[index], "\nmaking\n", newLayer
            result.replaceLayer(newLayer,index)

        return result

    def mutate(self):
        """
            Mutates stuff
            Return Type: <Organism>
        """
        for layer in self.getLayers():
            for gate in range(len(layer.gates)):
                if random.random() < .1:
                    #print "before mutation: ", layer.getGates()[gate]
                    layer.getGates()[gate].randomInitialize(self.numInputs)
                    #print "after mutation: ", layer.getGates()[gate]
        
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
