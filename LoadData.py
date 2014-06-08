'''
Created on 8 Jun 2014

@author: Zubin
'''
def LoadData(iFile):
    print 'Entering Load data'
    readData=open(iFile,'r')
    data=[]
    line=readData.readline()
    while line :
        line=line.strip('\n')
        line=line.strip('\t')
        data.append(line)
        line=readData.readline()
    return data

def Initialize(n):
    processedNodes=[1]
    remainingNodes=[]
    for i in range(2,n+1):
        remainingNodes.append(i)
    spDistance=[0]
    return processedNodes,remainingNodes,spDistance