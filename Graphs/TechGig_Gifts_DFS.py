''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
from collections import defaultdict
class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if  len(self.items)>0:
            return True
        else:
            return False

class Vertex():
    def __init__(self,key):
        self.key = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None
        self.Discovery=0

    def getColor(self):
        return self.color

    def getdistance(self):
        return self.distance

    def getDiscovery(self):
        return self.Discovery

    def getFinish(self):
        return self.Finish

    def getpred(self):
        return self.pred

    def setColor(self,color):
        self.color = color

    def setdistance(self,distance):
        self.distance = distance

    def setDiscovery(self, Discovery):
        self.Discovery = Discovery

    def setFinish(self, Finish):
        self.Finish = Finish

    def setpred(self,pred):
        self.pred = pred

    def addConnection(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def reset(self):
        # self.setColor('white')
        # self.setdistance(0)
        # self.setpred(None)
        self.color='white'
        self.distance=0
        self.pred=None
        self.Discovery=0
        self.Finish=0


class Graph():
    def __init__(self):
        self.vertexlist={}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVert = Vertex(key)
        self.vertexlist[key]=newVert
        return newVert

    def addEdge(self,f,t,cost=0):
        if f not in self.vertexlist:
            nv=self.addVertex(f)
        if t not in self.vertexlist:
            nv=self.addVertex(t)

        self.vertexlist[f].addConnection(self.vertexlist[t],cost)
        self.vertexlist[t].addConnection(self.vertexlist[f], cost)

    def getVertex(self, n):
        if n in self.vertexlist:
            return self.vertexlist[n]
        else:
            return None

    def getVertices(self):
        return self.vertexlist.keys()


    def __iter__(self):
        return iter(self.vertexlist.values())

    def reset(self):
        self.time = 0
        for key in self.getVertices():
            vert = self.getVertex(key)
            vert.reset()


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setpred(startVertex)
                self.dfsvisit(nextVertex)

            startVertex.setColor('black')
            self.time += 1
            startVertex.setFinish(self.time)


def traverse(s,e):
    path=[]
    path.append(e.key)
    if e is not None and e.getpred() is not None:
        while int(e.getpred().key)!=int(s.key):
            path.append(e.getpred().key)
            e=e.getpred()

    path.append(s.key)
    return path


def findmaxoccurence(L):
    d = defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])[1]
    print(result)


temp=input().split(" ")
M = int(temp[1])
N=int(temp[0])

gr=DFSGraph()

for i in range(N-1):
    temp=input().split(" ")
    gr.addEdge(int(temp[0]),int(temp[1]),0)

start=[]
end=[]

for i in range(M):
    temp = input().split(" ")
    start.append(int(temp[0]))
    end.append(int(temp[1]))

house_gift=[]

for i in range(len(start)):
    gr.reset()
    s_vert = gr.getVertex(start[i])
    e_vert = gr.getVertex(end[i])
    gr.dfsvisit(s_vert)
    path_list = traverse(s_vert,e_vert)
    house_gift.extend(path_list)

findmaxoccurence(house_gift)