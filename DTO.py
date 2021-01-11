class Vaccine:
    def __init__(self, id, date, supplier, quantity):
        self.id = int(id)
        self.date = date
        self.supplier = int(supplier)
        self.quantity = int(quantity)


class Supplier:
    def __init__(self, id, name, Logistics):
        self.id = int(id)
        self.name = name
        self.logistic = int(Logistics)


class Clinic:
    def __init__(self, id, location, demand, logistics):
        self.id = int(id)
        self.location = location
        self.demand = int(demand)
        self.logistic = int(logistics)


class Logistic:
    def __init__(self, id, name, count_Sent, count_Received):
        self.id = int(id)
        self.name = name
        self.count_Sent = int(count_Sent)
        self.count_Received = int(count_Received)
