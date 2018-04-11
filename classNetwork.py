import math

# Dictionaries
# Mapping Nodes with IDs

class edge:
    def __init__(self, weight):
        self.weight = weight
    
    def getWeight(self):
        return self.weight
        
    def setWeight(self, v):
        self.weight = v

class node:
    def __init__(self, bias, aType = 'step'):
        self.bias = bias
        self.inputs = []
        self.weights = []
        self.aType = aType
        self.out = 0
        
    def setInputs(self, inputs):
        self.inputs = inputs
    
    def actFunction(self, p):
        if self.aType == 'step':
            if p >= 0:
                return 1
            else:
                return 0
                
    def activate(self):
        p = 0
        for i in range(len(self.weights)):
            p += self.weights[i] * self.inputs[i]
        self.out = self.actFunction(p + self.bias)
        
class network:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.outputs = []
        self.inputs = []
    
    def addNode(self, n):
        self.nodes.append(n)
    
    def addEdge(self, n1, n2, w):
        self.edges.append((n1, n2, w))
        
    def setOut(self, outputs):
        self.outputs = outputs
    
    def setIn(self, inputs):
        self.inputs = inputs                        

    def step(self):
        for i in range(len(self.nodes)):
            self.nodes.setIntputs(
            self.nodes[i].activate()
            
    def getOut(self):
        ret = []
        for i in range(len(self.outputs)):
            ret.append(self.outputs[i].out)
        return ret
    
n = network()

a = node(0)
b = node(0)
c = node(0)

n.addNode(a)
n.addNode(b)
n.addNode(c)

n.addEdge(n.nodes[0], n.nodes[2], 0.5)
n.addEdge(n.nodes[1], n.nodes[2], -.1)

n.setOut([n.nodes[2]])
n.setIn([n.nodes[0], n.nodes[1]])


print(n.getOut())   
n.step()
print(n.getOut())          