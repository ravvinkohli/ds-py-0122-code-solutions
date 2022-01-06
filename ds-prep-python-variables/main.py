from types import ClassMethodDescriptorType


first_name = 'ravleen'
last_name = "kaur"
full_name = first_name + " " + last_name
print(full_name)
height_in_inches = 66
x = type(height_in_inches)
print(height_in_inches)
print(x)
y = height_in_inches_float = 66.0
print(y)
a = height_in_centimeters_float = y * 2.54
b = height_in_meters = a / 100
print(b)
eats_plants = True
eats_animals = False
is_animal = eats_plants or eats_animals
is_omnivore = eats_plants and eats_animals
is_plant = not(is_animal)
print(is_animal , is_omnivore , is_plant)
print(eats_plants or eats_animals)
print(not(eats_plants or eats_animals))
v = is_omnivore
mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860
print(height_in_meters == mean_height_in_meters)
is_mean_height = height_in_meters == mean_height_in_meters
is_short = height_in_meters < short_threshold_in_meters
is_tall = height_in_meters >= tall_threshold_in_meters
is_normal_height = height_in_meters >= short_threshold_in_meters and height_in_meters < tall_threshold_in_meters
print (is_mean_height , is_short , is_tall , is_normal_height)
nothing = None
print(nothing , type)
