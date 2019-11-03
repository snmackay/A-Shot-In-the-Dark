from parsing import parseItems,parseNodes
import objects

def start():
	itemsList=parseItems('items.csv')
	statesList=parseNodes('Nodes.csv')
	return(0, statesList, itemsList)

def traverse(node, user_input):
	if user_input not in node.children.keys():
		return (node.nodeId)
	return(node.children[user_input])