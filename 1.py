print("hello world")
print(type(4))
print(type(4.4))
print(type("kot"))
print(type(True))
lista = ["Ala", "ma", "kota", "i" ,"psa"]
print(type(lista))
krotka = (3,5,"kawa", True)
print(type(krotka))
slownik = {"kkk","jjj"}
print(type(slownik))
def listToString(s): 
    str1 = " " 
    return (str1.join(s))
print(listToString(lista)) 
znaki1= listToString(lista)
def stringToList(s):
    listRes = list(s.split(" "))
    return listRes
print(stringToList(znaki1))
zdanie="Metody Inżynieri Wiedzy są najlepsze"
zdanie1=zdanie.lower()
print(zdanie1, len(zdanie1))
zdanie2=zdanie1.replace("ż", "z")
zdanie2=zdanie2.replace("ą", "a")
print(zdanie2)
zdanie3=set(zdanie2)
print(zdanie3)
tupka=("Ala", "ma", "kota")
print(tupka)
lista1=[3,1,4,2]
lista2=["c","d","a","b"]
nowy=lista1+lista2
print(nowy)
print(nowy.index("c"))
