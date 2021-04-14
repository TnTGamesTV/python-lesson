from math import pi

def get_sphere_volume(radius):
    return 4 / 3 * pi * (radius ** 3);

def get_cylinder_volume(radius, height):
    return height * pi * (radius ** 2);

def get_cube_volume(length):
    return length ** 3;

def get_cuboid_volume(length, width, height):
    return length * width * height;

def get_pyramid_volume(length, height):
    return (1 / 3) * (length ** 2) * height;

print("Welchen Körper wollen Sie berechnen ?");
print("[1] Kugel");
print("[2] Zylinder");
print("[3] Würfel");
print("[4] Quader");
print("[5] Pyramide");

mode = input("Eingabe: ");

volume = 0;
if(mode == "1"):
    radius = int(input("Geben Sie den Radius an (cm): "));

    volume = get_sphere_volume(radius);

if(mode == "2"):
    radius = int(input("Geben Sie den Radius an (cm): "));
    height = int(input("Geben Sie die Höhe an (cm): "));

    volume = get_cylinder_volume(radius, height);

if(mode == "3"):
    length = int(input("Geben Sie die Länge an (cm): "));

    volume = get_cube_volume(length);

if(mode == "4"):
    length = int(input("Geben Sie den Länge an (cm): "));
    width = int(input("Geben Sie die Breite an (cm): "));
    height = int(input("Geben Sie die Höhe an (cm): "));

    volume = get_cuboid_volume(length, width, height);

if(mode == "5"):
    length = int(input("Geben Sie den Länge an (cm): "));
    height = int(input("Geben Sie die Höhe an (cm): "));

    volume = get_pyramid_volume(length, height);

print("Das Volumen deines Körpers ist: {} cm^3".format(volume));