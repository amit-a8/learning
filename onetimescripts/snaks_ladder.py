class Node:
    def __init__(self, value, sons = []):
        self.value = value
        self.sons = []
        self.has_parent = False
        for son in sons:
            self.sons.append(son)

    def add_son(self, node):
        self.sons.append(node)
        node.has_parent = True

    def delete_son_by_value(self, value):
        for s in self.sons:
            if s.value == value:
                s.has_parent = False #  ='(
                self.sons.remove(s)
                return True
        return False

    def number_of_sons(self):
        return len(self.sons)

    def nodes_in_tree_with_this_root(self):
        node_number = 1
        for son in self.sons:
            node_number += son.nodes_in_tree_with_this_root()
        return node_number

    def remove_extra_nodes(self):
        nodes_per_tree = {}
        removed = 0
        for son in self.sons: 
            nodes_per_tree[son.value] = son.nodes_in_tree_with_this_root()
        total_nodes = sum(nodes_per_tree.values()) + 1 
        if self.has_parent:
            total_nodes += 1 

        if total_nodes % 2 == 0:
            for node_value, number_of_sons in nodes_per_tree.items():
                if number_of_sons % 2 == 0 and number_of_sons > 0:  
                    self.delete_son_by_value(node_value)
                    total_nodes -= number_of_sons
                    removed += 1
        return removed

nodes = {}
nodes[1] = Node(1)
number_of_nodes = int(input().split(" ")[1])
for i in range(number_of_nodes):
    aux = input().split(" ")
    value, father = int(aux[0]), int(aux[1])
    nodes[value] = Node(value)
    nodes[father].add_son(nodes[value])

removed_nodes = 0
for node_id, node in nodes.items():
    removed_nodes += node.remove_extra_nodes()
print(removed_nodes)
