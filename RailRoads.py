from Spaces import Space
class RailRoad(Space):
    def __init__(self, name, val, rent, cost, mortgage, unmortgage):
        super().__init__(name, val, cost)
        self.rent = rent
        self.mortgate = mortgage
        self.unmortgage = unmortgage


# Properties("B & O Railroad", rent1=25, rent2=50, rent3=100, rent4=200, mortgage=100, unmortgage=110)