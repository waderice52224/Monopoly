from Spaces import Space
class Properties(Space):
    def __init__(self, name, val, rent, rentm, rent1, rent2, rent3, rent4, rent5, house, cost, mortgage, unmortgage):
        super().__init__(name, val, cost)
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







