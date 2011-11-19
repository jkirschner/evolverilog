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
        randomInit=False, nLayers=1, moduleName='organism'):
        
        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.moduleName = moduleName
        self.fitness = None
        self.layers = [None]*nLayers
        self.nLayers=nLayers
        self.nGates=numOutputs
        
        if randomInit:
            self.randomInitialize(self.nLayers, self.nGates)

    def randomInitialize(self, nLayers, nGates):
        """
            Return Type: void
        """
        for layer in range(nLayers):
            self.layers[layer] = Layer(nGates, randomInit=True)
    
    def crossover(self, otherOrganism):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
            Each layer of the resulting <Organism> is fully inherited from one parent.
        """
        return NotImplementedError, 'Crossover method from Organism must be overwritten.'
        
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
        return 'Organism: {\n%s, fitness: %s}'%(contents,str(self.fitness))
    
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
        """
        result = BooleanLogicOrganism(self.verilogFilePath, self.numInputs, self.numOutputs,  #change verilogFilePath??
            False, self.nLayers, self.moduleName)

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
            
class Layer:
    def __init__(self, nGates, randomInit=False):
        self.gates = [None]*nGates
        self.nGates = nGates
        if randomInit:
            self.randomInitialize(nGates)

    def randomInitialize(self, nGates):
        for gate in range(nGates):
            self.gates[gate] = Gate(nInputs=nGates,randomInit=True)  #In this case, we assume nGates maps to nInputs
            
    def addGate(self, gate):
        self.gates.append(gate)

    def getGates(self):
        return self.gates
    
    def getGate(self, index):
        return self.getGates()[index]

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
        ('buf',1),
        ('nand',2),
        ('xor',2)
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
    
    defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 4, 'fourBool',clearFiles=True)
    simMap = testOrgs.SimulationMap(defaultResult)
    
    a=BooleanLogicOrganism('fourBool.v',4,4,randomInit=True,moduleName='fourBool')
    b = a.evaluate(simMap)
    print a
    print b
    #testOrganism = BooleanLogicOrganism('',4,4,randomInit=True,moduleName='')
    #testOrganism.toVerilog('organismToVerilogTest.v','test')  
