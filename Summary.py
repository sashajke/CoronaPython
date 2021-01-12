class _Summary:
    def __init__(self):
        self.totalInventory = 0
        self.totalDemand = 0
        self.totalReceived = 0
        self.totalSent = 0
        self.filePath = ""
        self.file = None

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
        self.file = open(filePath, 'w')

    def shipmentReceived(self, amountReceived):
        self.setInventory(self.totalInventory + amountReceived)
        self.setReceived(self.totalReceived + amountReceived)

    def shipmentSent(self, amountSent):
        self.setInventory(self.totalInventory - amountSent)
        self.setDemand(self.totalDemand - amountSent)
        self.setSent(self.totalSent + amountSent)

    def saveToFile(self):
        list = [str(self.totalInventory), str(self.totalDemand), str(self.totalReceived), str(self.totalSent)]
        toWrite = ','.join(list)
        toWrite += '\n'
        self.file.write(toWrite)

    def close(self):
        self.file.close()


sum = _Summary()
