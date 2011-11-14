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

def verilogFromTemplate(moduleName,moduleArgs,moduleBody):

    template = """module %s(%s);\n\n%s\n\nendmodule"""
    
    return template%(moduleName,moduleArgs,moduleBody)

class Organism:
    
    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit=False, nLayers=1, nGates=4, moduleName='organism'):
        
        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.moduleName = moduleName
        self.fitness = None
        self.layers = [None]*nLayers
        self.nLayers=nLayers
        self.nGates=nGates
        if randomInit:
            self.randomInitialize(nLayers, nGates)

    def randomInitialize(self, nLayers, nGates):
        """
            Return Type: void
        """
        for layer in range(nLayers):
            self.layers[layer] = Layer(randomInit=True, nGates=nGates)
    
    def crossover(self, otherOrganism):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
        """
        pass

    def mutate(self):
        """
            Return Type: <Organism>
        """
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
        
        layerInputs = moduleInputs
        lastLayerIndex = len(self.layers)-1
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
        
    def __str__(self):
        contents = '\n'.join(str(layer) for layer in self.layers)
        return 'Organism: {\n' + contents + '}'
    
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
        if self.fitness is None:
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
    
    def addLayer(self, Layer):
        self.layers.append(Layer)

class BooleanLogicOrganism(Organism):
    
    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        
        score = 0.0
        for i, aOut, cOut in zip(inputs,actualOutputs,correctOutputs):
            if aOut == cOut:
                score += 1.0
        return score
        
    def crossover(self, otherParent):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
            Assumes both gates have the same # of layers, etc.
        """
        result = BooleanLogicOrganism(self.verilogFilePath, self.numInputs, self.numOutputs,  #change verilogFilePath??
        False, 0, 0, self.moduleName)
        selfLayers = self.getLayers()
        otherLayers = otherParent.getLayers()
        print "self length", len(selfLayers), "\n"
        print "other length", len(otherLayers)
        for index in range(len(selfLayers)):
            newLayer=selfLayers[index].crossover(otherLayers[index])
            print selfLayers[index], "\nLAYER crossing over with\n", otherLayers[index], "\nmaking\n", newLayer
            result.addLayer(newLayer)
        return result

class Layer:
    def __init__(self, randomInit=False, nGates=4):
        self.gates = [None]*nGates
        if randomInit:
            self.randomInitialize(nGates)

    def randomInitialize(self, nGates):
        for gate in range(nGates):
            self.gates[gate] = Gate(nInputs=nGates,randomInit=True)  #In this case, we assume nGates maps to nInputs
            
    def addGate(self, gate):
        self.gates.append(gate)
        
    def getGate(self, num):
        return self.gates[num]

    def crossover(self, otherLayer):
        """
            Return Type: <Layer>
            Crossovers self with another <Layer>, and returns a new <Layer>
        """
        offspring = Layer(nGates=0)
        for gate in range(len(self.gates)):
            offspring.addGate(random.choice([self.getGate(gate), otherLayer.getGate(gate)]))
        return offspring
        
    def __str__(self):
        contents = ' '.join(str(gate) for gate in self.gates)
        return 'Layer:[ ' + contents + ']'
        
    def toVerilog(self,inputNames,outputNames):
        
        txtLines = []
        for i,gate in enumerate(self.gates):
            gateInputs = ','.join(inputNames[c] for c in gate.inputConnections)
            gateOutput = outputNames[i]
            gateArgs = '%s,%s'%(gateOutput,gateInputs)
            txtLines.append('\t%s #%d (%s);'%(gate.gateType,gate.__delay__,gateArgs))
        return '\n'.join(txtLines)

class Gate:
    
    __delay__ = 50
    
    # type followed by number of inputs
    gateChoices = [
        ('and',2),
        ('or',2),
        ('not',1),
        ('buf',1)
        ]
    
    def __init__(self, nInputs, randomInit=False):
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
        self.gateType,gateInputs = random.choice(self.gateChoices)
        self.inputConnections = [random.randint(0,nInputs-1) for i in xrange(gateInputs)]
            
    def __str__(self):
        return self.gateType+str(self.inputConnections)
        
if __name__ == '__main__':
    #testOrganism = BooleanLogicOrganism('TestCode/andTest.v',2,1,randomInit=True,moduleName='andTest')
    #print testOrganism
    
    #defaultResult = testOrgs.testOrganism('TestCode/andTest.v', '.', 2, 1, 'andTest',clearFiles=True)
    #simMap = testOrgs.SimulationMap(defaultResult)
    
    #print testOrganism.evaluate(simMap)
    
    testOrganism = BooleanLogicOrganism('',4,4,randomInit=True,moduleName='')
    testOrganism.toVerilog('organismToVerilogTest.v','test')
