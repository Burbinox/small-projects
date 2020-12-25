"""
    Program makes new file (pliki.txt) where every car from first file (marki.txt) is one after the other. 
    It can be use to create database.
  """
cars = []

file = open('file.txt', encoding="utf8")
for line in file:
    cars.append(line)

del cars[::3]
del cars[1::2]

brands = open('brands.txt', "a+")

for car in cars:
    brands.write(car)

brands.close()
