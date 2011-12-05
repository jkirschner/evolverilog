import sys, os, subprocess, glob
sys.modules["ete2"]="ignore"
sys.modules["ete2a1"]="ignore"

#From OrganismManager.py
import testOrgs
import random
import selector
import matplotlib.pyplot as pyplot
from copy import deepcopy
import os
import cProfile
import pstats


import OrganismManager
import TreeOrganism

class ScootBotManager(OrganismManager.OrganismManager):
    def __init__(self, organismType, population, survival, mutateNum, threshold,    
        resultMap, verilogWriteFileName = 'organism.v', 
        verilogModuleName = None, numberOfInputs=5, numberOfOutputs=4, maxGeneration=100, **kwargs):
        """
            organisms  : <List> of <Organism>s
            population : the maximum number of <Organism>s
            survival   : the number of <Organism>s that will survive
                         each generation
            mutateNum  : the number of <Organism>s that will be only mutated
                         The other organisms will be crossovered, not mutated
            threshold  : fitness at which the simulation stops
            resultMap  : <testOrgs.SimulationMap> of correct behavior
        """
        assert (survival > 0), "At least one Organism should survive."
        assert (population > 0), "At least one Organism should exist."
        assert (population >= survival + mutateNum), \
                                         "population should be greater than " \
                                         "survival and mutateNum."
        
        self.generationNumber = 0
        
        self.organismType = organismType
        
        self.organisms = []
        self.population = population
        self.survival = survival
        self.mutateNum = mutateNum
        self.threshold = threshold
        self.maxGeneration = maxGeneration

        self.crossoverNum = population - (survival + mutateNum)
        
        #self._resultMap = resultMap
        #self._numberOfInputs = resultMap.getNumberOfInputs()
        self._numberOfInputs = numberOfInputs
        #self._numberOfOutputs = resultMap.getNumberOfOutputs()
        self._numberOfOutputs = numberOfOutputs

        
        self._selectorPmf = None
        
        self.verilogWriteFileName = verilogWriteFileName
        
        if verilogModuleName is None:
            verilogModuleName = verilogWriteFileName.split('.')[0]
            
        self.verilogModuleName = verilogModuleName
        
        self.kwargs = kwargs

    def getRandomOrganism(self):
            randOrganism = self.organismType(
                self.verilogWriteFileName,
                self.getNumberOfInputs(),
                self.getNumberOfOutputs(),
                randomInit=True,
                moduleName=self.verilogModuleName,
                **self.kwargs
                )
            
            randOrganism.evaluate(None)
            return randOrganism
    def updateOrganisms(self,visualize=False):
            """
                Return Type: void
                1. Keep (self.survival) <Organism>s from the
                   previous generation based on fitness
                2. Selects two <Organism>s from the list, crossover them and add
                   a new <Organism>
                3. Repeat 2. (population - survival) times
                4. Sort the list by their fitness.
            """
            newGeneration = [];
            generatorPmf = self._selectorPmf.Copy()
            for i in range(self.survival):
                replicatedOrganism = generatorPmf.Random()
                generatorPmf.Remove(replicatedOrganism)
                generatorPmf.Normalize()
                newGeneration.append(replicatedOrganism)
            
            generatorPmf = self._selectorPmf
            for i in range(self.mutateNum):
                replicatedOrganism = deepcopy(generatorPmf.Random())
                replicatedOrganism.mutate()
                newGeneration.append(replicatedOrganism)

            for i in range(self.crossoverNum):
                p1,p2 = self.generateParents()
                # print parent1, "\nORGANISM crossing over with\n", parent2
                newOrganism = p1.crossover(p2)
                newGeneration.append(newOrganism)
            
            map( lambda scootBotOrganism : scootBotOrganism.evaluate(None),
                 newGeneration)
            
            self.organisms = newGeneration
            self.organisms.sort(reverse = True)
            self._updateSelectorPmf()
            
            if visualize:
                self.visualize()

    def execute(self,visualize=False):
            """
                Return Type: void
                MainLoop
            """
            self.writeSimulation()
            self.populate(visualize)
            while self.organisms[0].getFitness() < self.threshold and self.generationNumber < self.maxGeneration:
                self.generationNumber += 1
                self.updateOrganisms(visualize)
            print "final fitness: ", self.organisms[0].getFitness()
            self.organisms[0].toVerilog('Winner.v', self.verilogModuleName)
            #self.deleteSimulation()


class ScootBotOrganism(TreeOrganism.TreeOrganism):
    treeCrossOverProbability = .7
    treeMutateProbability = .1
    def evaluate(self,correctResultMap):
        """
        Evaluates the fitness function of an organism if it has not
        already been evaluated.  The correctResultMap determines
        the correct mapping between inputs and outputs.
        
        Args:
            correctResultMap: testOrgs.SimulationMap
        
        Return type: <float> or <int> (number)
        """
        if self.fitness is None:
            self.toVerilog(self.verilogFilePath, self.moduleName)
            #change the arguments on the line below or it will not toVerilog
            testOutput = testScootBotOrganism(
                self.verilogFilePath,
                'TestCode',
                self.numInputs,
                self.numOutputs,
                self.moduleName,
                writeSim=False,
                clearFiles=False)

            self.fitness = self.fitnessFunction(testOutput)
            print self.fitness
            #print testOutput
            #print "fitness: ", self.fitness
            #raw_input("press enter yo")
          
        return self.fitness
    
    def fitnessFunction(self, testOutput):
        return testOutput[0].count('PickedUp')

    def crossover(self, otherParent):
        """
            Return Type: <ScootBotOrganism>
            Crossovers self with another <ScootOrganism>, and returns a new
            <ScootOrganism>.
        """
        result = ScootBotOrganism(self.verilogFilePath, self.numInputs,
            self.numOutputs, randomInit=False, maxDepth=self.maxDepth,
            inputProbability=self.inputProbability, moduleName=self.moduleName)
        for i in range(self.numOutputs):
            selfTree = self.trees[i]
            otherTree = otherParent.trees[i]
            if (random.random() > ScootBotOrganism.treeCrossOverProbability):
                #print "not crosovered"
                if (random.random() < .5):
                    result.trees.append(selfTree)
                else:
                    result.trees.append(otherTree)
            else:
                #print "crosovered"
                if (random.random() < .5):
                    result.trees.append(selfTree.crossover(otherTree))
                else:
                    result.trees.append(otherTree.crossover(selfTree))

        return result

    def mutate(self):
        """
            Return Type: void
            Mutates stuff
        """
        
        for i in range(len(self.trees)):
            if (random.random() < ScootBotOrganism.treeMutateProbability):
                self.trees[i].mutate()

def testScootBotOrganism(filepath, subdir, numInputs, numOutputs, 
    organismModuleName, clearFiles=True, testFileName = 'simulateScootBot2',
    writeSim=False):

    # write the verilog test file
    if writeSim:
        writeSimulation(
            os.path.join(subdir,'%s.v'%testFileName),
            filepath,
            numInputs,
            numOutputs,
            organismModuleName
            )
    
    # print 'Testing organism: %s'%filepath

    # compile the test file
    subprocess.call([
        'iverilog', '-o', 
        os.path.join(subdir,'%s.o'%testFileName),
        os.path.join(subdir,'%s.v'%testFileName)]
        )
    # get the test file results
    process = subprocess.Popen([
        'vvp',
        os.path.join(subdir,'%s.o'%testFileName)],
        stdout=subprocess.PIPE
        )
    # pull output from pipe
    output = process.communicate() #(stdout, stderr)
    
    if clearFiles:
        try:
            os.remove(os.path.join(subdir,'%s.o'%testFileName))
            os.remove(os.path.join(subdir,'%s.v'%testFileName))
        except:
            print "Error clearing files!"
            print "Files are to be cleared, but the files probably don't exist."
    
    return output

def main():
    import matplotlib.pyplot as pyplot
    import testOrgs
    from BooleanLogic import BooleanLogicOrganism
    from TreeOrganism import TreeOrganism
    
    pyplot.ion()
    manager = ScootBotManager(ScootBotOrganism,
        50,12,13,35,None,verilogWriteFileName = 'scootBot.v', #no simMap
        verilogModuleName="scootBot", maxDepth=3,inputProbability=.5, maxGeneration=100)
        
    manager.execute(True)
    pyplot.show()
    pyplot.ioff()

if __name__ == '__main__':
    main()