'''
Created on 8 Jun 2014

@author: Zubin
'''
maxDistance=1000000
seperator='\t'
def Get_Distance(i,data,spDistance):
    dMin=maxDistance
    jMin=0 
    info=data.split(seperator)
    if len(info)<=1 :
        return maxDistance,1
    for i in range(1,len(info)):
        temp=info[i].split(',')
        node=int(temp[0])
        dist=int(temp[1])
        if dMin>dist :
            dMin=dist
            jMin=node   
    #print '%%%',jMin,dMin       
    return dMin+spDistance,jMin


def Remove_Node(node,data):
    info=data.split(seperator)
    #print info
    if len(info)>1 :
        for i in range(1,len(info)):
            temp=info[i].split(',')
            #print temp
            if node==int(temp[0]) :
                info.pop(i)
                data=seperator.join(info)
                return data
    return data
       
        
                
                    
def PullNode(processedNodes,remainingNodes,spDistance,data):
    count=0
    minDistance=1000000000000
    jMinNode=0
    for i in processedNodes :
        #print '!!!!!',i,data[i-1],spDistance[count]
        #print data[i-1]
        dMin,jMin=Get_Distance(i,data[i-1],spDistance[count])
        if minDistance>dMin:
            minDistance=dMin
            jMinNode=jMin
        count+=1
        
    #print jMinNode,':',minDistance
    processedNodes.append(jMinNode)
    remainingNodes.remove(jMinNode)
    spDistance.append(minDistance) 
    for i in range(0,len(data)):
        data[i]=Remove_Node(jMinNode,data[i])
    #print data[0]


