class Vaccine:
    def __init__(self, id, date, supplier, quantity):
        self.id = id
        self.date = date
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, id, name, Logistics):
        self.id = id
        self.name = name
        self.logistic = Logistics


class Clinic:
    def __init__(self, id, location, demand, logistics):
        self.id = id
        self.location = location
        self.demand = demand
        self.logistic = logistics


class Logistic:
    def __init__(self, id, name, count_Sent, count_Received):
        self.id = id
        self.name = name
        self.count_Sent = count_Sent
        self.count_Received = count_Received
