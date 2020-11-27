# Std
from abc import ABC
# Util
from util.ray import ray
from util.vector import vec3

from Material import material

class hit_record():
    def __init__(self):
        self.p = vec3(0.0, 0.0, 0.0)
        self.normal = vec3(0.0, 0.0, 0.0)
        self.t = 100000000.0
        self.hitted = False
        self.material = material()

class hittable(ABC):
    def hit(self, r, t_min, t_max, hit_rec):
        raise NotImplementedError('Subclass must implement hit method')
