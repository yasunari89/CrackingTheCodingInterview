from node.graph_node import GraphNode

class DFS:
    def search(self, root: GraphNode, value):
        if root == None: return False
        root.marked = True
        if root.data == value: return True
        for child_node in root.children:
            if child_node.marked == False:
                if self.search(child_node, value):
                    return True
        return False