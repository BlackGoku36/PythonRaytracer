class ray :
    def __init__(self, origin, direction) :
        self.origin = origin
        self.direction = direction
    def origin(self):
        return self.origin
    def direction(self):
        return self.direction
    def point_at(self, t):
        return self.origin + self.direction * t
