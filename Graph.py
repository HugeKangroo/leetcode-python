'''
@Author: your name
@Date: 2020-03-25 15:32:03
@LastEditTime: 2020-03-25 21:29:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/Graph.py
'''

class Node(object):
    def __init__(self,key):
        self._id = key
        self._nbrs = {}

    def addNbrs(self,key,weight=0):
        self._nbrs[key] = weight

    def getNbrs(self):
        return self._nbrs.keys()

    def getID(self):
        return self._id

    def getWeight(self,key):
        return self._nbrs[key]


class Graph(object):
    def __init__(self):
        self._nodes = {}
        # self._edges = {}

    def addNode(self,key):
        self._nodes[key] = Node(key)
        return self._nodes[key]

    def addEdge(self,n1,n2,weight=0,directed=False):
        assert n1 != n2 ," n1, n2 can not be same."

        if n1 not in self._nodes.keys():
            node1 = self.addNode(n1)
        
        if n2 not in self._nodes.keys():
            node2 = self.addNode(n2)

        if directed:
            self._nodes[n1].addNbrs(n2,weight)
        else:
            self._nodes[n1].addNbrs(n2,weight)
            self._nodes[n2].addNbrs(n1,weight)

    def getEdge(self,n1,n2):
        # assert n1 != n2 ," n1, n2 can not be same."
        if n1 in self._nodes.keys and n2 in self._nodes.keys() and n1 != n2:
            node1 = self._nodes[n1]
            # node2 = self._nodes[n2]
            if n2 in node1.getNbrs():
                weight = node1.getWeight(n2)
                return weight
        
        raise ValueError("can not find valid edge weight")

    def __getitem__(self,n):
        return self._nodes.get(n)
    
    def getNode(self,n):
        return self.__getitem__(n)


def BFSearch(graph,start,target):
    visited = []
    queue = []
    queue.append(graph[start].getNbrs())
    visited.append(graph[start].getID())
    while len(queue) > 0:
        key = queue.pop(0)
        if key not in visited:
            if key == target:
                return True, visited
            else:
                queue += graph[key].getNbrs()
                visited.append(key)
    return False, None


if __name__ == "__main__":
    g = Graph()
    g.addNode(1)
    g.addNode(2)
    g.addEdge(3,5)
    g.addEdge(4,2)
    g.addEdge(4,5)
    BFSearch(g,1,5)