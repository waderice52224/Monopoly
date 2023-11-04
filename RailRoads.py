from Spaces import Space
class RailRoad(Space):
    def __init__(self, name, val, rent, cost, mortgage, unmortgage):
        super().__init__(name, val, cost)
        self.rent = rent
        self.mortgate = mortgage
        self.unmortgage = unmortgage
        self.owned = False

    def canbuy(self):
        return True

    def purchase(self):
        self.owned = True