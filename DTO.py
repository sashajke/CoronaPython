import datetime
class Vaccine:
    def __init__(self, id, date, supplier, quantity):
        self.id = int(id)
        # this next part is for modifying yyyy-mm-d format to yyyy-mm-dd format
        # if the 2nd letter from the end is not a digit it means we only have one digit at the day so we add 0 to it
        dateInChars = [letter for letter in date]
        if not dateInChars[-2].isdigit():
            dateInChars.insert(len(dateInChars)-1, '0')
            newdate = ""
            for letter in dateInChars:
                newdate += letter
            date = newdate
        self.date = date
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
