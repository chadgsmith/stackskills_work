import csv

with open("Wiggles_BaseLab_20170309-100643.csv", "r") as inventory:
    inventoryFile = csv.reader(inventory)
    output = open("InventoryOutput.csv", "a")
    outputWriter = csv.writer(output)

    newNode = 0
    for row in inventoryFile:
        if row and newNode:
            nodeName = row[0]
            cardType = row[1]
            slot = row[2]
            part = row[5]
            serial = row[7]
            if cardType == " <empty>":
                continue
            if part == " AdminUnlocked" or part == " AdminAutoInService":
                part = row[12]
            if part == " <empty>" or part == " <none>":
                continue
            else:
                outputWriter.writerow([nodeName, cardType, slot, part, serial])
                continue

            outputWriter.writerow([nodeName, cardType, slot, part, serial])
            continue
            if row[0] == "":
                newNode = 0
                continue
            else:
                continue
        if row and row[0] == "Node Name":
            newNode = 1
            continue
        else:
            newNode = 0
            continue

output.close()
inventory.close()