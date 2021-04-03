from math import pi

def get_sphere_surface(radius):
    return 4 * pi * (radius ** 2);

def get_sphere_volume(radius):
    return 4 / 3 * pi * (radius ** 3);

radius = int(input('Radius (cm): '));

diameter = radius * 2;
surface = get_sphere_surface(radius);
volume = get_sphere_volume(radius);

print('Deine Kugel mit dem Durchmesser {} cm, hat eine Oberfläche von {} cm² und ein Volumne von {} cm³.'.format(diameter, surface, volume));