#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

szam1= int(input('Adja meg az egyik számot! '))
szam2= int(input('Adja meg a masik szamot! '))

if szam1 > szam2:
  print('Két szám közül ez a nagyobb',szam1)
  
if szam1 < szam2:
  print('Ket szám közül ez a nagyobb', szam2)