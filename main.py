from Summary import sum
from Repository import repo
import DTO
import sys


def main(args):
    sum.setFilePath(args[3])
    readConfig(args[1])
    executeOrders(args[2])
    sum.close()
    repo.close()


def readConfig(filePath):
    config = open(filePath)
    amountOfEachPart = config.readline()[0:-1].split(',')
    # read the vaccines
    numOfVaccines = int(amountOfEachPart[0])
    for x in range(0, numOfVaccines):
        line = config.readline()
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
        if "\n" in line:
            logisticDetails = line[0:-1].split(',')
        else:
            logisticDetails = line.split(',')
        logistic = DTO.Logistic(*logisticDetails)
        repo.logistics.insert(logistic)
    config.close()


def executeOrders(filePath):
    orders = open(filePath)
    for order in orders:
        line = order.strip()
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

    orders.close()


if __name__ == '__main__':
    main(sys.argv)
