'''
Created on 8 Jun 2014

@author: Zubin
'''
from LoadData import LoadData,Initialize 
from ShowData import ShowData 
from PullNode import PullNode,Remove_Node

iFile='D:\\Assg1\\dijkstraData\\dijkstraData.txt'

def main():
    print 'Main Loop'
    data=LoadData(iFile)
    #ShowData(data)
    processedNodes,remainingNodes,spDistance=Initialize(len(data))
    for i in range(0,len(data)):
        data[i]=Remove_Node(1,data[i])
    #ShowData(data)
    
    while len(remainingNodes)>0:        
        PullNode(processedNodes,remainingNodes,spDistance,data)
        #print len(processedNodes),len(remainingNodes)
        #print spDistance
        #ShowData(data)
    #print remainingNodes
    #print processedNodes
    #print spDistance
    index=[7,37,59,82,99,115,133,165,188,197]
    #index=[11,12,13,14,15]
    test=[]
    for ind in index :
        k=processedNodes.index(ind)
        print processedNodes[k],spDistance[k]
        test.append(spDistance[k])
    print len(test),test
    
    
if __name__ == '__main__':
    main()