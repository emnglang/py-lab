
f = open("data.txt", "r") 
line = f.readline()
print(line)
Data = []
while len(line):
  if not line.startswith("#"):
    l = line.split() 
    Pres = float(l[0]) 
    Temp = float(l[1]) 
    Ene = float(l[2]) 
    Data.append([Pres, Temp, Ene]) 
  line = f.readline()
f.close()
print(Data)
