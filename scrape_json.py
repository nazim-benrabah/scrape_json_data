import re
from requests import *
from re import *

from pathlib import *
from json import *

from collections import defaultdict


####################################################  QESTION 1

url = ' https://opendata.paris.fr/explore/dataset/lieux-de-tournage-a-paris/download/?format=json&timezone=Europe/Berlin&lang=fr'


def stream_download(source_url, dest_file):
	r = get(source_url, stream=True)
	dest_file = Path(dest_file)
	with open(dest_file, "wb") as f:
		for chunk in r.iter_content(chunk_size=8192):
			if chunk:
				f.write(chunk)

stream_download(source_url=url, dest_file="exercice3.json")

with open('exercice3.json') as infile:
 data = load(infile)



####################################################  QESTION 2 

print("Il y'a en tout "+str(len(data))+"entree")



for i in range(len(data)):
	try:
		print("Entree "+str(i+1))
		print("Nom du realisateur : " +str(data[i]['fields']['nom_realisateur']))
		print("Titre : " +str(data[i]['fields']['nom_tournage']))
		print("Arrondissement : " +str(data[i]['fields']['ardt_lieu']))
		print("Date du debut : " +str(data[i]['fields']['date_debut']))
		print("Date de fin : " +str(data[i]['fields']['date_fin']))
		print("Coordonnees GPS : " +str(data[i]['fields']['geo_shape']['coordinates']))
		print('')

	except Exception:
		print('')

print("_______________________________________________________________________\n")


####################################################  QESTION 3

films=[]

index={}

for i in range(len(data)):
	films.append(data[i]['fields']['nom_tournage'])





def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)


for f in sorted(list_duplicates(films)):
	index[f[0]]=[]
	index[f[0]].append(f[1])



films = list(dict.fromkeys(films))

info={}

for f in films:
	info[f]=[]
	try:
		info[f].append({'Realisateur':str(data[index[f][0][0]]['fields']['nom_realisateur'])})
	except Exception:
		info[f].append({'Realisateur':'Realisateur introuvable'})

	try:
		info[f].append({'date':str(data[index[f][0][0]]['fields']['annee_tournage'])})
	except:
		info[f].append({'date':'Date introuvable'})

	try:
		for i in index[f][0]:
			
			info[f].append({'lieu':str(data[i]['fields']['adresse_lieu'])})

	except Exception:
		info[f].append({'lieu':' lieu introuvable'})


for f in films:
	try:
		print('Film :'+str(f))
		print(info[f])
		print("")

	except Exception:
		print("Une erreur s'est produite pour le film "+str(f))
		print('')
print("_______________________________________________________________________\n")


#################################################################################################### QESTION 4
arrondissement=[]
index_ardt={}

for i in range(len(data)):
	arrondissement.append(data[i]['fields']['ardt_lieu'])


for a in sorted(list_duplicates(arrondissement)):
	index_ardt[a[0]]=[]
	index_ardt[a[0]].append(a[1])


arrondissement = list(dict.fromkeys(arrondissement))
for a in sorted(arrondissement):
	try:
		print('Arrondissement : '+str(a) +'\n'+'Nombre de tournages : '+ str(len(index_ardt[a][0])))
		print('')
	except Exception:
		print('')

