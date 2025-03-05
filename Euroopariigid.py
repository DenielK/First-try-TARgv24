from random import *
def failist_to_dict(f:str):
    riik_pealinn={}#sõnastik {"Riik":"Pealinn"}'
    pealinn_riik={}
    riigid=[]
    file=open(f,'riigid_pealinnad',encoding"utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn,riigid
#käivitame loodud funkstion
riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")
riigid=list(riik_pealinn,keys())
#list riigid
print(riigid)
print(riik_pealinn.keys())
#list pealinnad
pealinnad=list(riik_pealinn.values())
print(pealinnad)
print(riik_pealinn.values())
              

#prindime riigide nimetused
while true:
    riik=input("Riik: ")
    if riik="A": break
    print("Pealinn",riik_pealinn[riik])

#Veerud riigid-pealinnad
for key,value in riik_pealinn.items():
    print(key+"-"+value+"\n")
