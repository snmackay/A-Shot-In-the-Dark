from enum import Enum
import csv
#created by veronica Vitale for UBHacking 2019

#classes

#item types
class ItemTypes(Enum):
	WEAPON = "Weapon"
	PHONE = "Phone"
	TECH = "Tech"
	MISC = "MISC."
	STABLE = "STABLE"
	CLOTHES = "Clothes"
	NULL_ITEM = "Veroinca WHAT THE FUCK"


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


#parsing


#parse nodes
def parseNodes(filename):
	nodeList = {}
	with open(filename) as f:
		csv_reader = csv.reader(f)
		csv_reader.next()
		for line in csv_reader:
			node = int(line[0])
			dia = line[1]
			itemList = parseNodeItems(line[2])
			adList = parseAdjacency(line[3])
			inspec = line[4]

			nodeList[node] = Node(node, dia, inspec, adList)
		f.close()
	return nodeList;
#creates diactionary of actions; key: nodeID, value: Action
def parseAdjacency(adList):
	splitList = adList.split("|")
	retVal = {}
	for item in splitList:
		splitItem = item.split(",")
		retVal[int(splitItem[0])] = splitItem[1]
	return retVal
#creates list of items in a node
def parseNodeItems(itemList):
	items = itemList[1:len(itemList)-1]
	return items.split(",")

#parse itmes
def parseItems(filename):
	itemList = {}
	with open(filename) as f:
		csv_reader = csv.reader(f)
		csv_reader.next()
		for line in csv_reader:
			iNum = int(line[0])
			iType = itemEnums(line[1])
			name = line[2]
			flavorText = line[3]
			itemList[iNum] = Items(iType, iNum, name, flavorText)
		f.close()
	return itemList
#set item to its enum
def itemEnums(typeString):
	if(typeString == "Weapon"):
		return ItemTypes.WEAPON
	if(typeString == "Phone"):
		return ItemTypes.PHONE
	if(typeString == "Tech"):
		return ItemTypes.TECH
	if(typeString == "MISC."):
		return ItemTypes.MISC
	if(typeString == "STABLE"):
		return ItemTypes.STABLE
	if(typeString == "Clothes"):
		return ItemTypes.CLOTHES
	return ItemTypes.NULL_ITEM

