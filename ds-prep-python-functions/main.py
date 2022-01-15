bool_to_int = lambda value: int(value)
print(bool_to_int(True))
get_smaller = lambda a , b: min(a , b)
print(get_smaller(5 , 10))
def cube(x):
  return x**3
print(cube(5))
def absolute_difference(a , b):
  return max(a , b) - min(a , b)
print(absolute_difference(3 , 5))
def squared_difference(a , b):
  return ((a - b)**2)
print(squared_difference(3 , 2))
def hours_to_minutes(hours):
  return (hours*60)
print(hours_to_minutes(hours = 2))
def get_circumference(radius):
  return(radius*2*3.14)
print(get_circumference(radius = 2))
def linear_transform(x , slope , intercept):
  return ((slope*x) + intercept)
print(linear_transform(x = 2 , slope = 3 , intercept = 2))
def standardize(x , x_center , scale_size):
  return((x - x_center) / scale_size)
print(standardize(x = 8 , x_center = 2 , scale_size = 2))
