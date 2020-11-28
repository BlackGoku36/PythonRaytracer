class ray :
    def __init__(self, origin, direction) :
        self.A = origin
        self.B = direction
    def origin(self):
        return self.A
    def direction(self):
        return self.B
    def point_at(self, t):
        return self.A + self.B * t
