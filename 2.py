lista1=[3,1,4,2]
lista2=["c","d","a","b"]
lista3=lista1.copy()
lista3.append(lista2)
lista2.extend(lista1)
print(lista3)
print(lista2)
slownik={'klucz1':'wartość1','klucz2':'wartość2'}
print(slownik)
print(slownik.keys())
print(bool(0))
for i in range(21):
    print(i)
tekst="Ala ma kota"
print(tekst.split(" "))
lista=[]
slowo=""
for i in tekst:
    if(i!=" "):
        slowo+=i
    else:
        lista.append(slowo)
        slowo=""
print(lista)
haslo="Haslo1234!"
flag1=False
flag2=False
flag3=False
flag4=False
if(len(haslo)>=10):
    flag1=True
for i in haslo:
    if(i.isupper()):
        flag2=True
    elif(i=="!"):
        flag3=True
    elif(i.islower()):
        flag4=True
if(flag1==True and flag2==True and flag3==True and flag4==True):
    print("haslo jest bezpieczne")
else:
    print("haslo nie jest bezpieczne")
liczby=[1,2,3,4,99]
for i in range(len(liczby)):
    if(liczby[i]!=99):
        print(liczby[i])

x=0
while x<len(liczby):
    if(liczby[x]==99):
        print(x)
        break
    else:
        x+=1

file1 = open("plik.txt","r")
for line in file1:
    print(line, end="")
print()
file1.close()
file1 = open("plik.txt","r")
print(file1.readlines())
print()

file1.close()
jezyki=["python","java","c++","c","c#"]
file2 = open("plik.txt","w")
for line in jezyki:
    print(line, file=file2)
file2.close()
