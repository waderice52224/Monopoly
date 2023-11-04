from Spaces import Space
class Utility(Space):
    def __init__(self, name, val, cost, mortgage, unmortgage):
        super().__init__(name, val, cost)
        self.mortgage = mortgage
        self.unmortgage = unmortgage
        self.owned = False

    def canbuy(self):
        return True

    def purchase(self):
        self.owned = True


