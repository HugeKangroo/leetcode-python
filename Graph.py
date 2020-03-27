'''
@Author: your name
@Date: 2020-03-25 15:32:03
@LastEditTime: 2020-03-27 16:34:09
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
        return list(self._nbrs.keys())

    def getID(self):
        return self._id

    def getWeight(self,key):
        weight = self._nbrs[key]
        if weight is None:
            raise ValueError("the weight from {0} to {1} is None.".format(self._id,key))
        else:
            return weight 


class Graph(object):
    def __init__(self):
        self._nodes = {}
        # self._edges = {}

    def addNode(self,key):
        if key not in self._nodes.keys():
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
        if n1 in self._nodes.keys() and n2 in self._nodes.keys() and n1 != n2:
            node1 = self._nodes[n1]
            # node2 = self._nodes[n2]
            if n2 in node1.getNbrs():
                weight = node1.getWeight(n2)
                return weight
        
        raise ValueError("can not find valid edge weight")

    def __getitem__(self,n):
        return self._nodes.get(n)
    
    def __iter__(self):
        for node in self._nodes:
            yield self._nodes[node]

    def getNode(self,n):
        return self.__getitem__(n)

    # def getNodes(self):
    #     return [ node for node in self._nodes]




def BFSearch(graph,start,target):
    visited = []
    queue = []
    queue += graph[start].getNbrs()
    visited.append(graph[start].getID())
    # path = [graph[start].getID()]
    path = []
    while len(queue) > 0:
        key = queue.pop(0)
        path.append(key)
        if key not in visited:
            if key == target:
                return True, path
            else:
                path.pop(-1)
                queue += graph[key].getNbrs()
                visited.append(key)
    return False, None

def Dijkstra(graph,start,target):
    def findMinCostNode(costs,visited):
        minCost = None
        minCostNode = None
        for k in costs:
            v = costs[k]
            if (minCost is None or  v < minCost) and (k  not in visited):
                minCost = v
                minCostNode = k
        return minCostNode,minCost
                

    s_node = graph[start]
    t_node = graph[target]
    parents={}
    visited = []
    costs = { node.getID(): float("inf") for node in graph if node != s_node }
    for nb in s_node.getNbrs():
        costs[nb] = s_node.getWeight(nb)
        parents[nb] = s_node.getID()

    cur_node = findMinCostNode(costs,visited)[0]
    while cur_node is not None:
        cur_cost = costs[cur_node]
        nbrs = graph[cur_node].getNbrs()
        for k in nbrs:
            next_cost = cur_cost + graph[cur_node].getWeight(k)
            if next_cost < costs[k]:
                costs[k] = next_cost
                parents[k] = cur_node
        visited.append(cur_node)
        cur_node = findMinCostNode(costs,visited)[0]
        
    path = []
    target = t_node.getID()
    path.append(target)
    while True:
        if target == s_node.getID():
            break
        target = parents[target]
        path.append(target)
    path.reverse()
    return path
    
    # while node 




if __name__ == "__main__":
    g = Graph()
    g.addEdge(1,2,5,True)
    g.addEdge(1,3,2,True)
    g.addEdge(3,2,8,True)
    g.addEdge(3,4,7,True)
    g.addEdge(2,4,2,True)
    g.addEdge(2,5,4,True)
    g.addEdge(5,4,6,True)
    g.addEdge(5,6,3,True)
    g.addEdge(4,6,1,True)
    # bl, path = BFSearch(g,1,5)
    path = Dijkstra(g,1,6)
    print(path)