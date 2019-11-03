#A Flash In the dark
#Started 11/2/2019
#Sean Mackay
#Veronica Vitale


import sys
from parsing import parseItems,parseNodes
import objects
from homeScreen import homeScreen
#pip3 install keyboard
import keyboard


#_______________________________________________________________________________
#traversal of states in game
#TODO validate
def traverse(startNode):
	currentNode = startNode
	while(currentNode is not None):
		print(currentNode.dialogue)
		print("Actions: ")
		for act in currentNode.children.keys():
			print("\t", act)
		user_val = input("")
		while user_val not in currentNode.children.keys():
			print("Command unknown")
			user_val = input("")
		currentNode = startNode.children[user_val]
#_______________________________________________________________________________

def main():
    itemsList=parseItems('items.csv')
    statesList=parseNodes('Nodes.csv')
    input=homeScreen()
    if input==0:
        traverse(statesList)
    elif input ==1:
        credits()


if "__name__==__main__":
    main()
