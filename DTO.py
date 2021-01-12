import datetime
class Vaccine:
    def __init__(self, id, date, supplier, quantity):
        self.id = int(id)
        dateParts = date.split('-')
        datePartsInt = [int(arg) for arg in dateParts]
        self.date = datetime.datetime(*datePartsInt).date()
        self.supplier = int(supplier)
        self.quantity = int(quantity)


class Supplier:
    def __init__(self, id, name, logistic):
        self.id = int(id)
        self.name = name
        self.logistic = int(logistic)


class Clinic:
    def __init__(self, id, location, demand, logistic):
        self.id = int(id)
        self.location = location
        self.demand = int(demand)
        self.logistic = int(logistic)


class Logistic:
    def __init__(self, id, name, count_sent, count_received):
        self.id = int(id)
        self.name = name
        self.count_Sent = int(count_sent)
        self.count_Received = int(count_received)
