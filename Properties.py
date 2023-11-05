from Spaces import Space


class Property(Space):
    def __init__(self, name, val, rent, rentm, rent1, rent2, rent3, rent4, rent5, house, typeSpace, cost, mortgage, unmortgage):
        super().__init__(name, val, typeSpace, cost)
        self.rent = rent
        self.rentm = rentm
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rent5 = rent5
        self.house = house
        self.cost = cost
        self.mortgage = mortgage
        self.unmortgage = unmortgage
        self.owned = False

    def canbuy(self):
        if not self.owned:
            return True
        return False

    def purchase(self):
        self.owned = True

    def getCost(self):
        return self.cost


