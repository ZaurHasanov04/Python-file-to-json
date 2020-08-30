import json

from lib import Student


users=[]

## funksiyalar yaradib datani json faylina yerlesdirmisem
## Data adinda dict yaradib icine users(isteye gore vermiyede bilersiz) "key"-ni verdim
data={}
data['users']=[]


## parametrli funksiya yaradib deyerleri donderdimki datanin icine novbeti funksiya vasitesile yerlesdire birim 
##qeyd edimki elave olaraq dict yaratdim(buda isteye goredi kim istese etmiye biler sadece olaraq yazilar daha anlamli olsun deye etdim)
def createdict(_name, _surname, _username, _password):
    innerdict={}
    innerdict['name']=_name
    innerdict['surname']=_surname
    innerdict['username']=_username
    innerdict['password']=_password
    return innerdict

def daxilet():
    name=input("Ad:")
    surname=input("Soyad:")
    username=input("Username:")
    password=input("Pass:")
    ## data['users']-ona gore yazdimki datanin icinde 'usersden sonra dict yaranacaq ve bu funksiyaya vereceyimiz deyerleri yuxaridaki funksiya alacaq ve data dict-nin icine yerlesdirecek
    data['users'].append(createdict(name,surname,username,password))
    return[name,surname,username,password]




def qeydiyyat():
    sayi=int(input("nece dene telebe elave etmek isteyirsiz:"))
    for user in range(sayi):
        user=Student(*daxilet())
        users.append(user)





def datanigoster():
    for user in users:
        user.show()



# Jsona cevirmek isteyirik

#######

            




print("1.Qeydiyyat elemek ucun 1 deymesin bas ")

ch=int(input("Reqem yaz:"))


if ch==1:
    qeydiyyat()
    datanigoster()
    
    



with open('dbs.json', "w") as connection:
    json.dump(data, connection)
    




    

        














