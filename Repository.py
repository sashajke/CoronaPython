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
        CREATE TABLE IF NOT EXISTS vaccines (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            supplier INTEGER ,
            quantity INTEGER NOT NULL ,
            FOREIGN KEY(supplier) REFERENCES suppliers(id)
        );

        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            logistic INTEGER ,
            FOREIGN KEY(logistic) REFERENCES logistics(id)
        );

        CREATE TABLE IF NOT EXISTS clinics (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            demand INTEGER NOT NULL ,
            logistic INTEGER ,
            FOREIGN KEY(logistic) REFERENCES logistics(id)
        );
        
        CREATE TABLE IF NOT EXISTS logistics (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             count_sent INTEGER NOT NULL ,
             count_received INTEGER NOT NULL
        );
        """)

    def receiveShipment(self, nameOfSup, amount, date):
        # insert the next vaccine to the vaccine table
        lastId = self.vaccines.getLastInsertedId()
        newVaccine = DTO.Vaccine(lastId + 1, date, nameOfSup, amount)
        self.vaccines.insert(newVaccine)
        # get the id of the logistics from the suppliers table using the name

        supplier = self.suppliers.find(name=nameOfSup)
        idOfLogistics = supplier.logistic

        # update the count_received of this logistics company in logistics table
        set_value = {"count_received": "count_received+" + str(amount)}

        # only where the id = idOfLogistics we got from the find query
        cond = {"id": idOfLogistics}
        self.logistics.update(set_value, cond)

    def sendShipment(self, locationOfClinic, amount):
        # remove amount from the demand of location
        set_value = {"demand": "demand - " + str(amount)}
        cond = {"location": locationOfClinic}
        self.clinics.update(set_value, cond)
        # remove amount from inventory
        allVaccines = self.vaccines.findWithASCOrder("date")
        for vaccine in allVaccines:
            if amount == 0:
                break
            if vaccine.quantity <= amount:
                self.vaccines.delete(id=vaccine.id)
            else:
                set_value = {"quantity": "quantity-" + str(amount)}
                cond = {"id": vaccine.id}
                self.vaccines.update(set_value, cond)

        # get the id of the logistic of this clinic
        clinic = self.clinics.find(location=locationOfClinic)
        idOfLogistics = clinic.logistic
        # update the count_sent of this logistics company in logistics table
        set_value = {"count_sent": "count_sent+" + str(amount)}

        # only where the id = idOfLogistics we got from the find query
        cond = {"id": idOfLogistics}
        self.logistics.update(set_value, cond)


repo = _Repository()
repo.create_tables()
