from collections import defaultdict

from Queue.QueueImplementation import Queue


class Vertex():
    def __init__(self,key):
        self.key = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.pred = None

    def getColor(self):
        return self.color

    def getdistance(self):
        return self.distance

    def getpred(self):
        return self.pred

    def setColor(self,color):
        self.color = color

    def setdistance(self,distance):
        self.distance = distance

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
        for key in self.getVertices():
            vert = self.getVertex(key)
            vert.reset()




temp=input().split(" ")
M = int(temp[1])
N=int(temp[0])

gr=Graph()

for i in range(N-1):
    temp=input().split(" ")
    gr.addEdge(int(temp[0]),int(temp[1]),0)

start=[]
end=[]

for i in range(M):
    temp = input().split(" ")
    start.append(int(temp[0]))
    end.append(int(temp[1]))

def getPath(s,e,g):
    s.setdistance(0)
    s.setpred(None)
    s.setColor('white')
    vertQ = Queue()
    vertQ.enqueue(s)
    path=[]
    while(vertQ.size()>0):
        currentV= vertQ.dequeue()
        currentV.setColor('black')
        for vert in currentV.getConnections():
            if (vert.getColor() == 'white'):
                vert.setColor('grey')
                vert.setdistance(currentV.getdistance() + 1)
                vert.setpred(currentV)
                vertQ.enqueue(vert)
            if int(vert.key)==int(e.key):
                path = traverse(s,vert)
                return path


def traverse(s,e):
    path=[]
    path.append(e.key)
    if e is not None and e.getpred() is not None:
        while int(e.getpred().key)!=int(s.key):
            path.append(e.getpred().key)
            e=e.getpred()

    path.append(s.key)
    return path

house_gift=[]

for i in range(len(start)):
    gr.reset()
    s_vert = gr.getVertex(start[i])
    e_vert = gr.getVertex(end[i])
    path_list = getPath(s_vert,e_vert,gr)
    house_gift.extend(path_list)

def findmaxoccurence(L):
    d = defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])[1]
    print(result)


findmaxoccurence(house_gift)