"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
<<<<<<< HEAD
    Date        : 11/19/2011
    File Name   : TreeOrganism.py
=======
    Date        : 11/24/2011
    File Name   : Tree.py
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d
    Description :
"""

import random
import Tree
from Organism import Organism
import testOrgs
import Organism
import Tree

class TreeOrganism(Organism):
<<<<<<< HEAD
    treeCrossOverProbability = .7

    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, maxDepth=10, inputProbability = .2, moduleName='organism'):
        # inputProbability should be reconsidered, and not just passed in
        # We should develop a way to decide what this value should be
=======
    
    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, maxDepth=4, moduleName='organism'):
        """
            Assumption: numOutputs = numTrees
        """
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d
        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.moduleName = moduleName
        self.fitness = None
<<<<<<< HEAD
        self.maxDepth = maxDepth
        self.inputProbability = inputProbability
        self.trees = []        
        
        if randomInit:
            self.randomInitialize()

    def __str__(self):
        contents = '\n'.join(str(tree) for tree in self.trees)
        return 'TreeOrganism: {\n%s, fitness: %s}'%(contents, str(fitness))
=======
        self.trees = [None]*numOutputs
        self.maxDepth = maxDepth
        if randomInit:
            self.randomInitialize()
        
    def __str__(self):
        contents = '\n Tree: '.join(str(tree) for tree in self.trees)
        return 'Trees: [\n %s ]\n' % contents
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d

    def randomInitialize(self):
        """
            Return Type: void
        """
<<<<<<< HEAD
        for i in range(self.numOutputs):
            self.trees.append(Tree(self.numInputs, self.maxDepth,
                                   self.inputProbability))
=======
        for tree in range(self.numOutputs):
            self.trees[tree] = Tree(numOrganismInputs = self.numInputs,
                                    maxDepth = self.maxDepth)
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d
    
    def crossover(self, otherOrganism):
        """
            Return Type: <TreeOrganism>
            Crossovers self with another <TreeOrganism>, and returns a new
            <TreeOrganism>.
<<<<<<< HEAD
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

    def toVerilog(self, filepath, moduleName):
        """
            Writes Organism to a verilog file.
        """
        
        moduleInputs = ['input%d'%i for i in xrange(self.numInputs)]
        moduleInputsTxt = ','.join(moduleInputs)
        moduleOutputsTxt = ','.join('output%d'%i for i in xrange(self.numOutputs))
        moduleArgsTxt = '%s,%s'%(moduleOutputsTxt,moduleInputsTxt)
        
        treeTxts = ['\toutput %s;'%moduleOutputsTxt,'\tinput %s;'%moduleInputsTxt]
        
        
        for layerNum,layer in enumerate(self.layers):
            
            if layerNum == lastLayerIndex:
                layerOutputs = ['output%d'%i for i in xrange(self.numOutputs)]
                layerOutputsTxt = '\twire %s;'%(','.join(layerOutputs))
            else:
                layerOutputs = ['layer%d_output%d'%(layerNum,i) for i in xrange(len(layer.gates))]
                layerOutputsTxt = '\twire %s;'%(','.join(layerOutputs))
            
            # call layer with inputs and outputs text
            layerTxt = layer.toVerilog(layerInputs,layerOutputs)
            layerTxts.append('\n%s\n\n%s'%(layerOutputsTxt,layerTxt))

            # at end of loop, the outputs of the last layer are inputs
            # to the new layer
            layerInputs = layerOutputs
        
        body = '\n'.join(layerTxts)
        fin = open(filepath,'w')
        fin.write(verilogFromTemplate(moduleName,moduleArgsTxt,body))
        fin.close()
        
    
    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        raise NotImplementedError, 'Override this method in sub-classes.'
        
    def evaluate(self,correctResultMap):
        """
        Evaluates the fitness function of an organism if it has not
        already been evaluated.  The correctResultMap determines
        the correct mapping between inputs and outputs.
        
        Args:
            correctResultMap: testOrgs.SimulationMap
        
        Return type: <float> or <int> (number)
        """
        if True:#self.fitness is None:
            self.toVerilog(self.verilogFilePath, self.moduleName)
            #change the arguments on the line below or it will not toVerilog
            simRes = testOrgs.testOrganism(
                self.verilogFilePath,
                'TestCode',
                self.numInputs,
                self.numOutputs,
                self.moduleName)
            
            inputs = []
            actualOutputs = []
            correctOutputs = []
            
            for trial in simRes.getTrials():
                currentInput = trial.getInputs()
                inputs.append(currentInput)
                actualOutputs.append(trial.getOutputs())
                correctOutputs.append(correctResultMap.getResult(currentInput))

            self.fitness = self.fitnessFunction(inputs,actualOutputs,correctOutputs)
          
        return self.fitness
            
    def getFitness(self):
        return self.fitness
        
    def __cmp__(self, other):
        return self.getFitness() - other.getFitness()
    
    def __hash__(self):
        return id(self)
        
    def getLayers(self):
        return self.layers
    
    def replaceLayer(self, layer, index):
        self.layers[index] = layer

class BooleanLogicOrganism(Organism):
    
    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        
        score = 0.0
        
        for i in xrange(self.nGates):
            if all( correctOutputs[idx][i] == a[i] for idx,a in enumerate(actualOutputs) ):
                score += 1.0
        return (score)**2 + 0.1
        
    def crossover(self, otherParent):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
            Assumes both gates have the same # of layers, etc.
=======
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d
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
<<<<<<< HEAD
    org = TreeOrganism( "", 4, 4, 
        False, 10, 5, 'organism')
    print org
##    defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 4, 'fourBool',clearFiles=True)
##    simMap = testOrgs.SimulationMap(defaultResult)
##    
##    a=BooleanLogicOrganism('fourBool.v',4,4,randomInit=True,moduleName='fourBool')
##    b = a.evaluate(simMap)
##    print a
##    print b
=======
    
    defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 4, 'fourBool',clearFiles=True)
    simMap = testOrgs.SimulationMap(defaultResult)
    
    a = TreeOrganism('fourBool.v',4,4,randomInit=True,moduleName='fourBool')
    b = a.evaluate(simMap)
    print a
    print b
>>>>>>> 9aef8d4bf61cfa1bfd7557da640f6fe7a0857e9d
    #testOrganism = BooleanLogicOrganism('',4,4,randomInit=True,moduleName='')
    #testOrganism.toVerilog('organismToVerilogTest.v','test')  
