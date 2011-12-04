class AbstractTerminator:
    
    def __init__(self,maxNumberOfGenerations):
        
        self.maxNumberOfGenerations = maxNumberOfGenerations
        self.success = False
        self.currentBestOrganism = None
        
    def isFinished(self,organism,generationNumber):
        raise NotImplementedError
        
    def getSuccess(self):
        return self.success
        
    def getBestOrganism(self):
        return self.currentBestOrganism
