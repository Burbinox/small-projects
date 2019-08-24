import linecache
"""
    Program makes new file (pliki.txt) where every car from first file (marki.txt) is one after the other. 
    It can be use to create database.
  """
Cars=[]

i = 2
plik = open('plik.txt',encoding="utf8")
for line in plik:
    Cars.append(linecache.getline('plik.txt', i))
    i = i + 3
j=0
for car in Cars:
   Cars[j]=Cars[j].strip()
   j = j + 1

print(Cars)
plik.close()

plik2 = open('marki.txt',"a+")

for car in Cars:
   plik2.write(car)
   plik2.write("\n")

plik2.close()


