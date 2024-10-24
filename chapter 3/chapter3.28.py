import math

a = 6378137.0
c = 6356752.314245

e2 = 1 - (c**2 / a**2)
e = math.sqrt(e2)

S_ellipsoid = 2 * math.pi * a**2 * (1 + ((1 - e2) / e) * math.tanh(e))

R = 6371000.0
S_sphere = 4 * math.pi * R**2

S_ellipsoid_km2 = S_ellipsoid / 1e6
S_sphere_km2 = S_sphere / 1e6

print(f"Площадь поверхности эллипсоида: {S_ellipsoid_km2} км")
print(f"Площадь поверхности сферы: {S_sphere_km2} км²")