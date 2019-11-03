from objects import Items, Node, ItemTypes
import csv
# ______________________________________________________________________________
# parses Nodes.csv
# creates diactionary of actions; key: Action, value: NodeID


def parseAdjacency(adList):
    print(adList)
    splitList = adList.split("|")
    retVal = {}
    for item in splitList:
        splitItem = item.split(",")
        retVal[splitItem[1]] = int(splitItem[0])
    return retVal

# creates list of items in a node


def parseNodeItems(itemList):
    items = itemList[1:len(itemList)-1]
    items.split(", ")
    # for i in items:
    #    i.replace(" ", "")
    return items

# main parsing function for game states (nodes)


def parseNodes(filename):
    nodeList = {}
    with open(filename) as f:
         csv_reader = csv.reader(f)
         next(csv_reader)
         for line in csv_reader:
             node = int(line[0])
             dia = line[1]
             itemList = parseNodeItems(line[2])
             adList = parseAdjacency(line[3])
             inspec = line[4]
             nodeList[node] = Node(node, dia, inspec, adList)
         f.close()
    return nodeList

# _______________________________________________________________________________
# parses items.csv

# sets items from csv to their correct type

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

# main parser function for items

def parseItems(filename):
    itemList = {}
    with open(filename) as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            iNum = int(line[0])
            iType = itemEnums(line[1])
            name = line[2]
            flavorText = line[3]
            itemList[iNum] = Items(iType, iNum, name, flavorText)
        f.close()
    return itemList
