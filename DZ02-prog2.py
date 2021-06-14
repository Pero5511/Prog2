#ZADACA s CSV
#tutorial csv to list
import csv
with open('rezultati.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(map(tuple,reader))
your_list.sort()
#print (your_list)

new_list=[]
for ime, prezime, bodovi in your_list:
    new_list.append((prezime, ime, bodovi))
new_list.sort()

for prezime, ime, bodovi in new_list:
    print(bodovi, prezime, ime)

print("-" *60)

ocjene={'1':0,'2':0,'3':0,'4':0,'5':0}
for prezime, ime, bodovi in new_list:
    if int(bodovi) < 50:
        ocjene[str(1)]+=1
    elif int(bodovi) <65:
        ocjene[str(2)]+=1
    elif int(bodovi) <81:
        ocjene[str(3)]+=1
    elif int(bodovi) <91:
        ocjene[str(4)]+=1
    else:
        ocjene[str(5)]+=1
print(ocjene)
