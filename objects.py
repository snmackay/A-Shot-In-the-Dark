from enum import Enum

#object definitions for item types and node
#item types
class ItemTypes(Enum):
	WEAPON = "Weapon"
	PHONE = "Phone"
	TECH = "Tech"
	MISC = "MISC."
	STABLE = "STABLE"
	CLOTHES = "Clothes"
	NULL_ITEM = "Veronica WHAT THE FUCK"


#node class
class Node:
	def __init__(self, nodeId, dialogue, inspect, children):
		self.nodeId = nodeId
		self.dialogue = dialogue
		self.inspect = inspect
		self.children = children
#item class
class Items:
	def __init__(self, itype, iId, name, description):
		self.itype = itype
		self.iId = iId
		self.name = name
		self.description = description
