"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : OrganismManager.py
    Description :
"""

import random
import testOrgs

class Organism:
    def __init__(self, randomInit=False, nLayers=1, nGates=4):
        self.fitness = None
        self.layers = [None]*nLayers
        if randomInit:
            self.randomInitialize(nLayers, nGates)

    def randomInitialize(self, nLayers, nGates):
        """
            Return Type: void
        """
        for layer in range(nLayers):
            self.layers[layer] = Layer(randomInit=True, nGates=nGates)
        return

    def crossover(self, otherOrganism):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
        """
        return

    def mutate(self):
        """
            Return Type: <Organism>
        """
        return
        
    def __str__(self):
        contents = ''
        for layer in self.layers:
            contents += layer.__str__() + '\n'
        return 'Organism: {\n' + contents + '}'
        
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
            #change the arguments on the line below or it will not compile
            #simRes = testOrgs.testOrganism(<FILE1>,<DIR1>,<numIn>,<numOut>,<andTest>,clearFiles=True)
            #for trial in simRes:
            #    actualOutput = trial.getOutputs()
            #    expectedOutput = correctResultMap.getOutputs(trial.getInputs())
            #do some computation here to calculate the fitness
            #then return the fitness

            return 0 # Change this code
        else:
            return self.fitness

class Layer:
    def __init__(self, randomInit=False, nGates=4):
        self.gates = [None]*nGates
        if randomInit:
            self.randomInitialize(nGates)

    def randomInitialize(self, nGates):
        for gate in range(nGates):
            self.gates[gate] = Gate(randomInit=True, nInputs=nGates)  #In this case, we assume nGates maps to nInputs

    def crossover(self, otherLayer):
        """
            Return Type: <Layer>
            Crossovers self with another <Layer>, and returns a new <Layer>
        """
        return
        
    def __str__(self):
        contents = ' '.join(str(gate) for gate in self.gates)
        return 'Layer:[ ' + contents + ']'


class Gate:
    
    # type followed by number of inputs
    gateChoices = [
        ('and',2),
        ('or',2),
        ('not',1),
        ('buf',1)
        ]
    
    def __init__(self, randomInit=False, nInputs=4):
        self.inputConnections = []
        self.gateType = ''
        if randomInit:
            self.randomInitialize(nInputs)
            

    def randomInitialize(self, nInputs):
        """
            Return Type: void
            Randomly initializes its instruction and connection
						Assumes there are no prior connections
        """
        choice = random.choice(self.gateChoices)
        self.gateType = choice[0]
        for connection in range(choice[1]):
            self.inputConnections.append(random.randint(1,nInputs))
            
    def __str__(self):
        return self.gateType+str(self.inputConnections)
        
if __name__ == '__main__':
    testOrganism = Organism(randomInit=True)
    print testOrganism
