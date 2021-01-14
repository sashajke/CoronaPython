from Summary import sum
from Repository import repo
import DTO
import sys


def readConfig(filePath):
    with open(filePath, "r") as config:
        amountOfEachPart = config.readline()[0:-1].split(',')
        numOfVaccines = int(amountOfEachPart[0])
        # first read the vaccines
        for x in range(0, numOfVaccines):
            line = config.readline()
            # remove \n at the end of each line if exists
            if "\n" in line:
                vaccineDetails = line[0:-1].split(',')
            else:
                vaccineDetails = line.split(',')
            vaccine = DTO.Vaccine(*vaccineDetails)
            repo.vaccines.insert(vaccine)
            sum.totalInventory += int(vaccineDetails[3])
        # read the suppliers
        numOfSuppliers = int(amountOfEachPart[1])
        for i in range(0, numOfSuppliers):
            line = config.readline()
            # remove \n at the end of each line if exists
            if "\n" in line:
                supplierDetails = line[0:-1].split(',')
            else:
                supplierDetails = line.split(',')
            supplier = DTO.Supplier(*supplierDetails)
            repo.suppliers.insert(supplier)
        # read the clinics
        numOfClinics = int(amountOfEachPart[2])
        for i in range(0, numOfClinics):
            line = config.readline()
            # remove \n at the end of each line if exists
            if "\n" in line:
                clinicDetails = line[0:-1].split(',')
            else:
                clinicDetails = line.split(',')
            clinic = DTO.Clinic(*clinicDetails)
            repo.clinics.insert(clinic)
            sum.totalDemand += int(clinicDetails[2])
        # read the logistics
        numOfLogistics = int(amountOfEachPart[3])
        for i in range(0, numOfLogistics):
            line = config.readline()
            # remove \n at the end of each line if exists
            if "\n" in line:
                logisticDetails = line[0:-1].split(',')
            else:
                logisticDetails = line.split(',')
            logistic = DTO.Logistic(*logisticDetails)
            repo.logistics.insert(logistic)


def executeOrders(filePath):
    with open(filePath) as orders:
        for order in orders:
            line = order.strip()
            # remove \n at the end of each line if exists
            if "\n" in line:
                orderParts = line.split[0:-1](',')
            else:
                orderParts = line.split(',')
            if len(orderParts) == 3:
                repo.receiveShipment(*orderParts)
                sum.shipmentReceived(int(orderParts[1]))
            else:
                repo.sendShipment(*orderParts)
                sum.shipmentSent(int(orderParts[1]))
            sum.saveToFile()


if __name__ == '__main__':
    sum.setFilePath(sys.argv[3])
    readConfig(sys.argv[1])
    executeOrders(sys.argv[2])
    sum.close()
    repo.close()

