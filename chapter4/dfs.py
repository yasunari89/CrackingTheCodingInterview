from graph_node import GraphNode

class DFS:
    def search(self, root: GraphNode):
        if root == None: return
        root.marked = True
        print(root)
        for child_node in root.children:
            if child_node.marked == False:
                self.search(child_node)


root = GraphNode(0)
graph_node1 = GraphNode(1)
graph_node2 = GraphNode(2)
graph_node3 = GraphNode(3)
root.children.append(graph_node1)
root.children.append(graph_node2)
root.children.append(graph_node3)
graph_node1.children.append(GraphNode(4))
graph_node1.children.append(GraphNode(5))
graph_node1.children.append(GraphNode(6))

dfs = DFS()
dfs.search(root)