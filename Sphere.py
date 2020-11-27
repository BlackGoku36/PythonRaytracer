# Std
from math import sqrt
# Util
from util.ray import ray
from util.vector import vec3

import Hittable
from Material import material, lambertian

class sphere(Hittable.hittable):
    def __init__(self, pos, radius, mesh_material=lambertian(vec3(0.5, 0.5, 0.5))):
        self.pos = pos
        self.radius = radius
        self.mesh_material = mesh_material

    def hit(self, ray, t_min, t_max, hit_rec):
        oc = ray.origin() - self.pos
        ray_dir = ray.direction()
        a = vec3.dot(ray_dir, ray_dir)
        b = vec3.dot(oc, ray_dir)
        c = vec3.dot(oc, oc) - self.radius ** 2

        D = b**2 - a*c

        if D > 0.0 :
            temp = ( -b - sqrt( D ) ) / a
            if temp > t_min and temp < t_max :
                hit_rec.t = temp
                hit_rec.p = ray.point_at(hit_rec.t)
                hit_rec.normal = vec3.normalize(hit_rec.p - self.pos)
                hit_rec.material = self.mesh_material
                hit_rec.hitted = True
                return hit_rec

            temp = ( -b + sqrt( D ) ) / a
            if temp > t_min and temp < t_max :
                hit_rec.t = temp
                hit_rec.p = ray.point_at(hit_rec.t)
                hit_rec.normal = vec3.normalize(hit_rec.p - self.pos)
                hit_rec.hitted = True
                hit_rec.material = self.mesh_material
                return hit_rec

        hit_rec.hitted = False
        return hit_rec
