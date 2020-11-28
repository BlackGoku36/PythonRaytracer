# STD
import math
import time
from random import random
# Util
import util.color
from util.ray import ray
from util.vector import vec3

from Sphere import sphere
from Hittable import hit_record
from Material import material, lambertian, metal

from tqdm import tqdm

def shoot_ray(r, object_list, depth=0):
	rec = hit_record()
	for obj in object_list:
		rec = obj.hit(r, 0.01, rec.t, rec)
		if rec.hitted == True: break

	if rec.hitted == True:
		material = rec.material
		m_rec = material.scatter(r, rec)
		if depth < 10 and m_rec.bScattered == True:
			return m_rec.attenuation * shoot_ray( m_rec.scattered_ray, object_list, depth + 1)
		else:
			return vec3(0.0, 0.0, 0.0)

	dir = r.direction()
	t = (dir.y + 1.0) * 0.5
	return vec3.interpolate(vec3(0.3, 0.5, 0.8), vec3(1.0, 1.0, 1.0), t)

def renderer():
	aspect_ratio = 16/9
	image_width = 720
	image_height = int(image_width/aspect_ratio)
	num_samples = 50

	viewport_height = 2.0
	viewport_width = aspect_ratio * viewport_height
	focal_length = 1.0

	origin = vec3(0, 0, 0)
	horizontal = vec3(viewport_width, 0, 0)
	vertical = vec3(0, viewport_height, 0)
	lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)

	object_list =[
		sphere(vec3(-0.5, -0.5, -1.5), 0.5, lambertian(vec3(1.0, 0.8, 1.0))),
		sphere(vec3(0.5, -0.5, -1.5), 0.5, metal(vec3(1.0, 1.0, 1.0), 0.0)),
		sphere(vec3(0.5, 0.5, -1.5), 0.5, lambertian(vec3(0.8, 1.0, 1.0))),
		sphere(vec3(-0.5, 0.5, -1.5), 0.5, metal(vec3(1.0, 1.0, 1.0), 0.3))
		]

	file = open('output.ppm', 'w')

	file.write("P3\n{0:d} {1:d}\n255\n".format(image_width, image_height))
	pbar = tqdm(desc="Pixels rendered: ",total=image_height*image_width)
	for y in range(image_height-1, -1, -1):
		for x in range(image_width):
			color = vec3(0.0, 0.0, 0.0)
			for s in range(num_samples) :
				u = (x + random()) / float(image_width)
				v = (y + random()) / float(image_height)
				r = ray(origin, lower_left_corner + u*horizontal + v*vertical - origin)
				color = color + shoot_ray(r, object_list)
			color = color / float(num_samples)
			util.color.write_color(file, color)
			pbar.update(1)
	file.close()
	pbar.close()

start = time.time()
renderer()
end = time.time()
print(str(end - start)+" secs took to render")
