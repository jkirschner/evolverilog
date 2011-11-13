"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : Evaluator.py
    Description :
"""

import testOrgs

# WE MAY BE DELETING THIS
'''
class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, organism):
        """
            Return Type: Float
            Evaluates the fitness of the input organism, and returns it.
        """
        pass
'''
    
if __name__ == '__main__':
    
    defaultResult = testOrgs.testOrganism('TestCode/andTest.v', '.', 2, 1, 'andTest',clearFiles=True)
    simMap = testOrgs.SimulationMap(defaultResult)
    print simMap
    print simMap.getResult((1,1))
