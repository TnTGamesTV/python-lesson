class Bestellung:

    def __init__(self):
        self.orders = []
        self.amount = 0.0

    def addSpeisen(self, id):
        self.orders.append(id)

        if id == "Döner":
            self.amount += 5
        if id == "Pizza":
            self.amount += 6.8
        if id == "Burger":
            self.amount += 4.5

    def addGetraenk(self, id):
        self.orders.append(id)
        self.amount += 2

    def addMenue(self, id, idGetraenk):
        if id == 1:
            self.orders.append("Menü 1: Pizza mit einer {}".format(idGetraenk))
            self.amount += 8

        if id == 2:
            self.orders.append(
                "Menü 2: Döner und Pommes mit einer {}".format(idGetraenk))
            self.amount += 7

        if id == 3:
            self.orders.append(
                "Menü 3: Burger und Pommes mit einer {}".format(idGetraenk))
            self.amount += 6.5

    def zettel(self):
        for order in self.orders:
            print(order)

    def rechnung(self):
        print("Ihre Rechnung beläuft sich auf {}€".format(self.amount))


finn = Bestellung()    
finn.addSpeisen("Pizza")     
finn.addGetraenk("Cola")     
finn.addMenue(1, "Fanta")     
finn.addMenue(3, "Sprite")     
finn.addSpeisen("Pizza")     
finn.addSpeisen("Döner")     
finn.addSpeisen("Burger")     
finn.addMenue(2, "Cola")     
finn.zettel()     
finn.rechnung()