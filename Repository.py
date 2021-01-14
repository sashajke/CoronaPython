import sqlite3

# The Repository
from DAO import Dao
import DTO


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = Dao(DTO.Vaccine, self._conn)
        self.suppliers = Dao(DTO.Supplier, self._conn)
        self.clinics = Dao(DTO.Clinic, self._conn)
        self.logistics = Dao(DTO.Logistic, self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE IF NOT EXISTS logistics (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             count_sent INTEGER NOT NULL ,
             count_received INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            logistic INTEGER REFERENCES logistics(id)
        );

        CREATE TABLE IF NOT EXISTS clinics (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            demand INTEGER NOT NULL ,
            logistic INTEGER REFERENCES logistics(id)
        );
        CREATE TABLE IF NOT EXISTS vaccines (
            id INTEGER PRIMARY KEY,
            date DATE NOT NULL,
            supplier INTEGER REFERENCES suppliers(id),
            quantity INTEGER NOT NULL
        );
        """)

    def receiveShipment(self, nameOfSup, amount, date):
        # insert the next vaccine to the vaccine table
        # get the id of the logistics from the suppliers table using the name

        supplier = self.suppliers.find(name=nameOfSup)
        supplierIndex = supplier[0].id
        # get the id of the last inserted line to create a new id for the new vaccine
        lastId = self.vaccines.getLastInsertedId()
        newId = lastId[0] + 1
        newVaccine = DTO.Vaccine(newId, date, supplierIndex, amount)
        self.vaccines.insert(newVaccine)

        idOfLogistics = supplier[0].logistic

        # update the count_received of this logistics company in logistics table
        logistic = self.logistics.find(id=idOfLogistics)
        currCountRec = logistic[0].count_Received
        set_value = {'count_received': currCountRec + int(amount)}

        # only where the id = idOfLogistics we got from the find query
        cond = {'id': idOfLogistics}
        self.logistics.update(set_value, cond)

    def sendShipment(self, locationOfClinic, amount):
        clinic = self.clinics.find(location=locationOfClinic)
        # get the id of the logistic of this clinic

        idOfLogistics = clinic[0].logistic
        # update the count_sent of this logistics company in logistics table
        logistic = self.logistics.find(id=idOfLogistics)
        currCountSent = logistic[0].count_Sent

        set_value = {'count_sent': currCountSent + int(amount)}

        # only where the id = idOfLogistics we got from the find query
        cond = {"id": idOfLogistics}
        self.logistics.update(set_value, cond)
        # remove amount from inventory
        allVaccines = self.vaccines.findWithASCOrder('date')
        tempAmount = int(amount)
        for vaccine in allVaccines:
            if tempAmount == 0:
                break
            # we need to delete the line since the quantity will be zero

            if vaccine.quantity <= int(tempAmount):
                self.vaccines.delete(id=vaccine.id)
                tempAmount = tempAmount - int(vaccine.quantity)
            # if we can take amount and not delete

            else:
                set_value = {'quantity': vaccine.quantity - int(tempAmount)}
                cond = {"id": vaccine.id}
                self.vaccines.update(set_value, cond)
                tempAmount = 0

        # remove amount from the demand of location

        currDemand = clinic[0].demand

        set_value = {"demand": currDemand - int(amount)}
        cond = {"location": locationOfClinic}
        self.clinics.update(set_value, cond)


repo = _Repository()
repo.create_tables()
