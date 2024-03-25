from datetime import datetime 
import requests
import json

def ri3valeur(L):
  L1=[]
  for i in range(0,len(L),3):
      L1.append(L[i])
  return L1
dateLyouma=datetime.today().strftime("%Y-%m-%d")
lyoumaName=datetime.today().strftime("%A")
jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi', 'Thursday':'jeudi', 'Friday':'Vendredi', 'Saturday':'samedi','Sunday':'Dimanche'}
Lyouma=jours[lyoumaName]
url="https://api.open-meteo.com/v1/forecast?latitude=31,51&longitude=-9,77&hourly=temperature_2m&hourly=windspeed_10m&hourly=cloud_cover&hourly=precipitation&start_date="+dateLyouma+"&end_date="+dateLyouma
response=requests.get(url)
response=requests.get(url).content.decode('utf-8')
data = json.loads(response)

daytemperature=data[0]["hourly"]["temperature_2m"]
windsliste=data[0]["hourly"]["windspeed_10m"]
cloudcover=data[0]["hourly"]["cloud_cover"]
precipitation=data[0]["hourly"]["precipitation"]

listetemperature=ri3valeur(daytemperature)
listewind=ri3valeur(windsliste)
listcloud=ri3valeur(cloudcover)
listprecipitation=ri3valeur(precipitation)

def getImagescloud(L):
   listImages=[]
   for t in L:
      if t<20:
         listImages.append("sun.jpg")
      elif t<40:
         listImages.append("sunlowcloud.jpg")
      elif t<60:
         listImages.append("sunmorecloud.jpg")
      else :
         listImages.append("cloud.jpg")
   return listImages
listImagescloud=getImagescloud(listcloud)