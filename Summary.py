class _Summary:
    def __init__(self):
        self.totalInventory = 0
        self.totalDemand = 0
        self.totalReceived = 0
        self.totalSent = 0
        self.filePath = ""

    # update the inventory, increase is boolean to know if to increase or decrease
    def setInventory(self, amountToUpdate):
        self.totalInventory = amountToUpdate

    # update the demand, increase is boolean to know if to increase or decrease
    def setDemand(self, amountToUpdate):
        self.totalDemand = amountToUpdate

    # update the total received, increase is boolean to know if to increase or decrease
    def setReceived(self, amountToUpdate):
        self.totalReceived = amountToUpdate

    # update the total sent, increase is boolean to know if to increase or decrease
    def setSent(self, amountToUpdate):
        self.totalSent = amountToUpdate

    def setFilePath(self, filePath):
        self.filePath = filePath

    def shipmentReceived(self, amountReceived):
        self.updateInventory(self.totalInventory + amountReceived)
        self.updateReceived(self.totalReceived + amountReceived)

    def shipmentSent(self, amountSent):
        self.updateInventory(self.totalInventory - amountSent)
        self.updateDemand(self.totalDemand - amountSent)
        self.updateSent(self.totalSent + amountSent)

    def saveToFile(self):
        file = open(self.filePath, "w+")
        list = [self.totalInventory, self.totalDemand, self.totalReceived, self.totalSent]
        toWrite = ','.join(list)
        toWrite += '\n'
        file.write(toWrite)
        file.close()


sum = _Summary()
