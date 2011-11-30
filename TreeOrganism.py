"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/24/2011
    File Name   : TreeOrganism.py    
    Description :
"""

import random
import testOrgs
import Organism
import Tree

class TreeOrganism(Organism.AbstractOrganism):

    treeCrossOverProbability = .7

    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, maxDepth=10, inputProbability = .2, moduleName='organism'):
        # inputProbability should be reconsidered, and not just passed in
        # We should develop a way to decide what this value should be

        self.maxDepth = maxDepth
        self.inputProbability = inputProbability
        self.trees = []        
        
        print moduleName,'here'
        Organism.AbstractOrganism.__init__(self, verilogFilePath, 
            numInputs, numOutputs, randomInit=randomInit, 
            moduleName=moduleName)
            
    def __str__(self):
        contents = '\n-\n'.join(str(tree) for tree in self.trees)
        return 'TreeOrganism: {\n%s, fitness: %s}'%(contents, str(self.fitness))

    def randomInitialize(self):
        """
            Return Type: void
        """
        for i in range(self.numOutputs):
            self.trees.append(
                Tree.Tree(
                    self.numInputs, self.maxDepth,self.inputProbability)
                )
    
    def crossover(self, otherParent):
        """
            Return Type: <TreeOrganism>
            Crossovers self with another <TreeOrganism>, and returns a new
            <TreeOrganism>.
        """
        result = TreeOrganism(self.verilogFilePath, self.numInputs,
            self.numOutputs, randomInit=False, maxDepth=self.maxDepth,
            inputProbability=self.inputProbability, moduleName=self.moduleName)
        for i in range(self.numOutputs):
            selfTree = self.trees[i]
            otherTree = otherParent.trees[i]
            if (random.random() > TreeOrganism.treeCrossOverProbability):
                print "not crosovered"
                if (random.random() < .5):
                    result.trees.append(selfTree)
                else:
                    result.trees.append(otherTree)
            else:
                print "crosovered"
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
        moduleInputs = ['input%d'%i for i in xrange(self.numInputs)]
        moduleInputsTxt = ','.join(moduleInputs)
        moduleOutputsTxt = ','.join('output%d'%i for i in xrange(self.numOutputs))
        moduleArgsTxt = '%s,%s'%(moduleOutputsTxt,moduleInputsTxt)
        
        layerTxts = ['\toutput %s;'%moduleOutputsTxt,'\tinput %s;'%moduleInputsTxt]
        
        for idx,tree in enumerate(self.trees):
            # self.gate -> what type of gate it is
            layerTxts.append(tree.toVerilog(idx)+'\n')
        
        body = '\n'.join(layerTxts)
        
        fin = open(filepath,'w')
        fin.write(Organism.verilogFromTemplate(moduleName,moduleArgsTxt,body))
        fin.close()

    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        """
            Return Type: float
        """
        # Needs to be implemented #
        
        score = 0.0
        
        for i in xrange(self.numOutputs):
            if all( correctOutputs[idx][i] == a[i] for idx,a in enumerate(actualOutputs) ):
                score += 1.0
        return (score)**2 + 0.1
        
    def getTrees(self):
        return self.trees
    
    def replaceTree(self, tree, index):
        self.trees[index] = tree
        
if __name__ == '__main__':
    
    #defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 2, 'fourBool',clearFiles=True)
    #simMap = testOrgs.SimulationMap(defaultResult)
    
    #a = TreeOrganism('fourBool.v',4,2,randomInit=True,moduleName='fourBool')
    #b = a.evaluate(simMap)
    #print a
    #print b

    tree1 = TreeOrganism('tree.v',4,2,randomInit=True,moduleName='tree')
    tree2 = TreeOrganism('tree.v',4,2,randomInit=True,moduleName='tree')

    print "--------------------------------------"
    print tree1
    print "--------------------------------------"
    print tree2
    print "--------------------------------------"
    print tree1.crossover(tree2)
    print "--------------------------------------"
    print "--------------------------------------"
    print tree1
    #tree1.toVerilog('delme.v','delme')
    #print 'toVerilog() method test successful (no errors)'
