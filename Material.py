# Std
from abc import ABC
# Util
from util.ray import ray
from util.vector import vec3

class material_record :
    def __init__(self) :
        self.bScattered = False
        self.scattered_ray = ray(vec3(0.0, 0.0, 0.0), vec3(0.0, 0.0, 0.0))
        self.attenuation = vec3(0.0, 0.0, 0.0)

# material interface
class material(ABC) :
    def scatter(self, r, hit_rec) :
        raise NotImplementedError("Subclass must implement scatter method")

class lambertian(material) :
    def __init__(self, albedo) :
        self.albedo = albedo

    def scatter(self, r, hit_rec) :
        target = hit_rec.p + hit_rec.normal + vec3.get_random_in_sphere()

        m_record = material_record()
        m_record.scattered_ray = ray(hit_rec.p, target - hit_rec.p)
        m_record.attenuation = self.albedo
        m_record.bScattered = True

        return m_record

class metal(material) :
    def __init__(self, albedo, fuzz) :
        self.albedo = albedo
        self.fuzz   = min(fuzz, 1.0)

    def scatter(self, r, hit_rec) :
        reflected = vec3.reflect(vec3.normalize(r.direction()), hit_rec.normal)
        direction = reflected + self.fuzz * vec3.get_random_in_sphere()

        m_record = material_record()
        m_record.scattered_ray = ray(hit_rec.p, direction)
        m_record.attenuation = self.albedo
        m_record.bScattered = vec3.dot( m_record.scattered_ray.direction(), hit_rec.normal ) > 0

        return m_record
