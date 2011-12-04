"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : OrganismManager.py
    Description :
"""

import testOrgs

def verilogFromTemplate(moduleName,moduleArgs,moduleBody):

    template = """module %s(%s);\n\n%s\n\nendmodule"""
    
    return template%(moduleName,moduleArgs,moduleBody)

class AbstractOrganism:
    
    def __init__(self, verilogFilePath, numInputs, numOutputs, 
        randomInit = False, moduleName = None):
        
        self.verilogFilePath = verilogFilePath
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.fitness = None
        self.numCorrectOutputs = 0
        
        if moduleName is None:
            moduleName = verilogFilePath.split('.')[0]
        self.moduleName = moduleName
        
        if randomInit:
            self.randomInitialize()
        
    def randomInitialize():
        raise NotImplementedError, 'Must be overriden.'
        
    def toVerilog():
        raise NotImplementedError, 'Must be overriden.'
        
    def crossover():
        raise NotImplementedError, 'Must be overriden.'
    
    def mutate():
        raise NotImplementedError, 'Must be overriden.'
        
    def fitnessFunction(self,inputs,actualOutputs,correctOutputs):
        # must set number of correct outputs
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
            self.toVerilog(self.verilogFilePath, self.moduleName)
            #change the arguments on the line below or it will not toVerilog
            simRes = testOrgs.testOrganism(
                self.verilogFilePath,
                'TestCode',
                self.numInputs,
                self.numOutputs,
                self.moduleName,
                writeSim=False,
                clearFiles=False)
            
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
        
if __name__ == '__main__':
    #testOrganism = BooleanLogicOrganism('TestCode/andTest.v',2,1,randomInit=True,moduleName='andTest')
    #print testOrganism
    
    #defaultResult = testOrgs.testOrganism('TestCode/andTest.v', '.', 2, 1, 'andTest',clearFiles=True)
    #simMap = testOrgs.SimulationMap(defaultResult)
    
    #print testOrganism.evaluate(simMap)
    
    from BooleanLogic import BooleanLogicOrganism
    
    defaultResult = testOrgs.testOrganism('fourBoolCorrect.v', '', 4, 4, 'fourBool',clearFiles=True)
    simMap = testOrgs.SimulationMap(defaultResult)
    
    a=BooleanLogicOrganism('fourBool.v',4,4,randomInit=True,moduleName='fourBool')
    b = a.evaluate(simMap)
    print a
    print b
    #testOrganism = BooleanLogicOrganism('',4,4,randomInit=True,moduleName='')
    #testOrganism.toVerilog('organismToVerilogTest.v','test')  
