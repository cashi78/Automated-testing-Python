from address import Address


class Mailing:
    def __init__(self, _to_address=Address(), _from_address=Address(),
                 _cost=0, _track=""):
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track
