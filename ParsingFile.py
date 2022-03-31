from ctypes import sizeof
from typing import List
from xml.etree.ElementTree import tostring
import pandas as pd

DataClient = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATACLIENT.xlsx",skiprows=[0,1,2,3,4,5,507,506])


DataClient = DataClient.loc[:, ~DataClient.columns.isin(['Cv obligatoire ','adresse du siège','nom entreprise','Si non, souhaitez-vous vous plus d\'informations ?','Connaissez vous la différence de ces contrats ?','code NAF ', 'siret de l\'entreprise','prénom','nom','un site internet'])]


DataClient = pd.concat([DataClient[col].astype(str).str.lower() for col in DataClient.columns],axis=1)
 



##################################################################################################################################################################################################

#################################################TRAITEMENT POUR LE FICHIER DATACLIENT###################################################################################################################

##################################################################################################################################################################################################

 #Définission de la taille de l'entreprise sous forme de nombres tq:
#1=TPE
#2=PME
#3=ETI
#4=Grand Groupe

DataClient['Taille entreprise'] = DataClient['Taille entreprise'].map({
                             'tpe (1 à 10)':1,
                             'pme (10 à 50)':2,
                             'eti (50 à 500)':3,
                             'grand groupe (plus de 500 personnes)':4,
                             },)

#Définission des critère oui/ non par 0 et 1
#1=Oui
#0=Non

DataClient['Plusieurs personnes recherchées'] = DataClient['Plusieurs personnes recherchées'].map({
                             'oui':1,
                             'non':0,
                             },)                            

#Définission des critère oui/ non par 0 et 1
#1=Oui
#0=Non
DataClient['autre permis'] = DataClient['autre permis'].map({
                             'oui':1,
                             'non':0,
                             },)        

 #Définission des différents type de contrat:
 # contrat aidé ou aménagé (travailleur handicapé) = 0
 #temps partagé = 1
#bénévolat=2
#militaire = 3
#vdi (vendeur à domicile indépendant) = 4
#contrat sénior = 5
#mannequinat = 6
#indépendant / franchisé (eurl, sarl, sasu) = 7
#intérim = 8
#prêt de personnel = 9
#cdic (bâtiment) = 10
#cdd =11
#cdi = 12
#extra (restauration, hôtellerie)= 13
#alternance-appentissage=14
#vie / vte = 15
#titulaire de la fonction publique = 16
#Sous-traitance (Microentreprise)=17
#saisonnier = 18
#Stage = 19
#Portage salarial = 20
#intermitent (spectacle)= 21


DataClient['Quels types de contrats pour les embauchés - TEXTE'] = DataClient['Quels types de contrats pour les embauchés - TEXTE'].map({
                             'contrat aidé ou aménagé (travailleur handicapé)':'0',
                             'temps partagé':1,
                             'bénévolat' : 2,
                             'militaire' : 3,
                             'vdi (vendeur à domicile indépendant)' : 4,
                             'contrat sénior': 5,
                             'mannequinat': 6,
                             'indépendant / franchisé (eurl, sarl, sasu)':7,
                             'intérim':8,
                             'prêt de personnel' :9,
                             'cdic (bâtiment)': 10,
                             'cdd' : 11,
                             'cdi': 12,
                             'extra (restauration, hôtellerie)': 13,
                             'alternance-appentissage' : 14,
                             'vie / vte':15,
                             'titulaire de la fonction publique': 16,
                             'sous-traitance (microentreprise)':17,
                             'saisonnier': 18,
                             'stage':19,
                             'portage salarial' : 20,
                             'intermitent (spectacle)' : 21,
                             },)                            
#Data Mobilité:
#transport en commum = 0
#Permis de conduire / voiture = 1
#Permis 2 roue = 2
DataClient['Mobilité'] = DataClient['Mobilité'].map({
                             'transports en commun':0,
                             'voiture':1,
                             'permis de conduire':1,
                             'véhicule 2 roues':2,
                             },)        


DataListOfCompetences = list(DataClient.groupby(['Comptétences pour le poste 1']).groups)

for i in range(len(DataClient)):
    for j in range(len(DataListOfCompetences)):
        if DataClient['Comptétences pour le poste 1'][i] == DataListOfCompetences[j]:
                DataClient['Comptétences pour le poste 1']= DataClient['Comptétences pour le poste 1'].replace(DataListOfCompetences[j],j)
        if DataClient['Comptétences pour le poste 2'][i] == DataListOfCompetences[j]:
                DataClient['Comptétences pour le poste 2'] = DataClient['Comptétences pour le poste 2'].replace(DataListOfCompetences[j],j)
        if DataClient['Comptétences pour le poste 3'][i] == DataListOfCompetences[j]:
                DataClient['Comptétences pour le poste 3'] = DataClient['Comptétences pour le poste 3'].replace(DataListOfCompetences[j],j)



DataListOfPostLocation = list(DataClient.groupby(['Localisation du poste']).groups)
for i in range(len(DataClient)):
    for j in range (len(DataListOfPostLocation)):
            if DataClient['Localisation du poste'][i] == DataListOfPostLocation[j]:
                    DataClient['Localisation du poste'] = DataClient['Localisation du poste'].replace(DataListOfPostLocation[j],j)

DataListOfDiffJobs = list(DataClient.groupby(['Métier du poste']).groups)
for i in range(len(DataClient)):
    for j in range (len(DataListOfDiffJobs)):
            if DataClient['Métier du poste'][i] == DataListOfDiffJobs[j]:
                    DataClient['Métier du poste'] = DataClient['Métier du poste'].replace(DataListOfDiffJobs[j],j)

DataClient.to_csv("DataClientParsed.csv")                    

##################################################################################################################################################################################################

###################################################################TRAITEMENT POUR LE FICHIER JOBBEUR ######################################################################################################################

##################################################################################################################################################################################################

DataJobbeur = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATAJOBEUR.xlsx",skiprows=[0,1,2,3,4,5])

DataJobbeur = DataJobbeur.loc[:, ~DataJobbeur.columns.isin(['GENRE','NOM','Prénom','CODE POSTAL','Permis PL','Caces 1','Caces 2','Caces 3','Connaissez vous la différence entre ces types de contrats ?','Si non, souhaitez-vous vous plus d\'informations ?','Si vous avez un profil Linkedin ou un e-CV, coller le lien URL :','Si vous avez un site internet, blog ou portfolio coller le lien URL'])]


DataJobbeur = pd.concat([DataJobbeur[col].astype(str).str.lower() for col in DataJobbeur.columns],axis=1)

colsToReplaceWithTypeContract = ['Quel type de contrat vous intéresse 1','Quel type de contrat vous intéresse 2','Quel type de contrat vous intéresse 3']

DataJobbeur[colsToReplaceWithTypeContract] = DataJobbeur[colsToReplaceWithTypeContract].replace({
                             'contrat aidé ou aménagé (travailleur handicapé)':'0',
                             'temps partagé':1,
                             'bénévolat' : 2,
                             'militaire' : 3,
                             'vdi (vendeur à domicile indépendant)' : 4,
                             'contrat sénior': 5,
                             'mannequinat': 6,
                             'indépendant / franchisé (eurl, sarl, sasu)':7,
                             'intérim':8,
                             'prêt de personnel' :9,
                             'cdic (bâtiment)': 10,
                             'cdd' : 11,
                             'cdi': 12,
                             'extra (restauration, hôtellerie)': 13,
                             'alternance-appentissage' : 14,
                             'vie / vte':15,
                             'titulaire de la fonction publique': 16,
                             'sous-traitance (microentreprise)':17,
                             'saisonnier': 18,
                             'stage':19,
                             'portage salarial' : 20,
                             'intermitent (spectacle)' : 21,
                            'alternance, appentissage': 14,
                            'vdi (vendeur à doicile indépendant)': 4,

                             },)     


for i in range(len(DataJobbeur)):
    for j in range (len(DataListOfPostLocation)):
            if DataJobbeur['VILLE'][i] == DataListOfPostLocation[j]:
                    DataJobbeur['VILLE'] = DataJobbeur['VILLE'].replace(DataListOfPostLocation[j],j)
            elif (j==len(DataListOfPostLocation)-1 and isinstance(DataJobbeur['VILLE'][i],str)):         #DataJobbeur['VILLE'] = DataJobbeur['VILLE'].replace(DataJobbeur['VILLE'][i],-1)
                  DataJobbeur['VILLE'] = DataJobbeur['VILLE'].replace(DataJobbeur['VILLE'][i],-1)

for i in range(len(DataJobbeur)):
    for j in range (len(DataListOfPostLocation)):
            if DataJobbeur['Localisation géographique du poste (région, ville)'][i] == DataListOfPostLocation[j]:
                    DataJobbeur['Localisation géographique du poste (région, ville)'] = DataJobbeur['Localisation géographique du poste (région, ville)'].replace(DataListOfPostLocation[j],j)
            elif (j==len(DataListOfPostLocation)-1 and isinstance(DataJobbeur['Localisation géographique du poste (région, ville)'][i],str)):    
                       DataJobbeur['Localisation géographique du poste (région, ville)'] = DataJobbeur['Localisation géographique du poste (région, ville)'].replace(DataJobbeur['Localisation géographique du poste (région, ville)'][i],-1)


DataJobbeur['Quelle taille d\'entreprise / organisation TEXTE'] = DataJobbeur['Quelle taille d\'entreprise / organisation TEXTE'].map({
                             'tpe':1,
                             'pme':2,
                             'eti':3,
                             'grand groupe':4,
                             },)
                      

#Data Mobilité:
#transport en commum = 0
#Permis de conduire / voiture = 1
#Permis 2 roue = 2
TmpTableTransport = ['Voitures','Autre transports']
DataJobbeur[TmpTableTransport] = DataJobbeur[TmpTableTransport].replace({
                             'pas de véhicule':0,
                             'nan':0,
                             'transports en commun':0,
                             'vélo':0,
                             'véhiculé avec voiture':1,
                             'permis de conduire':1,
                             'deux roues à moteur':2,
                             'cyclomoteur':2,
                             },)    

for i in range(len(DataJobbeur)):
    for j in range(len(DataListOfCompetences)):
       # print(j)
        if DataJobbeur['Vos compétences 1'][i] == DataListOfCompetences[j]:
                DataJobbeur['Vos compétences 1']= DataJobbeur['Vos compétences 1'].replace(DataListOfCompetences[j],j)
        elif (j==len(DataListOfCompetences)-1 and isinstance(DataJobbeur['Vos compétences 1'][i],str)):        
                 DataJobbeur['Vos compétences 1'] = DataJobbeur['Vos compétences 1'].replace(DataJobbeur['Vos compétences 1'][i],-1)
        if DataJobbeur['Vos compétences 2'][i] == DataListOfCompetences[j]:
                DataJobbeur['Vos compétences 2'] = DataJobbeur['Vos compétences 2'].replace(DataListOfCompetences[j],j)
        elif (j==len(DataListOfCompetences)-1 and isinstance(DataJobbeur['Vos compétences 2'][i],str)):    
                 DataJobbeur['Vos compétences 2'] = DataJobbeur['Vos compétences 2'].replace(DataJobbeur['Vos compétences 2'][i],-1)

        if DataJobbeur['Vos compétences 3'][i] == DataListOfCompetences[j]:
                DataJobbeur['Vos compétences 3'] = DataJobbeur['Vos compétences 3'].replace(DataListOfCompetences[j],j)
        elif (j==len(DataListOfCompetences)-1 and isinstance(DataJobbeur['Vos compétences 3'][i],str)):
              DataJobbeur['Vos compétences 3'] = DataJobbeur['Vos compétences 3'].replace(DataJobbeur['Vos compétences 3'][i],-1)


colsToReplaceBy0And1 = ['Permis B','TPE - moins de 10 personnes','0- 20klm','PME 10 à 250 personnes','ETI 250 à 5000','GRAND GROUPE - Plus de 500 personnes','21- 40klm','Seriez-vous prêt à déménager pour ce futur job ?','61 - klm et plus','41-60klm']

DataJobbeur[colsToReplaceBy0And1] = DataJobbeur[colsToReplaceBy0And1].replace({
                                'oui':1,
                                'non':0,
                                'nan':0,})


for i in range(len(DataJobbeur)):
    for j in range (len(DataListOfDiffJobs)):
            if DataJobbeur['Dernier poste occupé (ou actuel)'][i] == DataListOfDiffJobs[j]:
                    DataJobbeur['Dernier poste occupé (ou actuel)'] = DataJobbeur['Dernier poste occupé (ou actuel)'].replace(DataListOfDiffJobs[j],j)
            elif (j==len(DataListOfDiffJobs)-1 and isinstance(DataJobbeur['Dernier poste occupé (ou actuel)'][i],str)):
                  DataJobbeur['Dernier poste occupé (ou actuel)'] = DataJobbeur['Dernier poste occupé (ou actuel)'].replace(DataJobbeur['Dernier poste occupé (ou actuel)'][i],-1)
for i in range(len(DataJobbeur)):
        for j in range (len(DataListOfDiffJobs)):
            if DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'][i] == DataListOfDiffJobs[j]:
                    DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'] = DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'].replace(DataListOfDiffJobs[j],j)
            elif (j==len(DataListOfDiffJobs)-1 and isinstance(DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'][i],str)):
                  DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'] = DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'].replace(DataJobbeur['Mission recherchée : Exemple n°1 de poste (métier + secteur)'][i],-1)
                                   

DataJobbeur.to_csv("DataJobbeurParsed.csv")                    
my_jobbers = ["1"]*len(DataJobbeur)
for i in range(len(DataJobbeur)):
    my_jobbers[i]='Jobbeur '+str(i)

MyDataResult = pd.DataFrame(columns=my_jobbers)
my_client = [1]*len(DataClient)



for i in range(len(DataClient)):
    my_client[i]=0
 

for i in range (len(DataJobbeur)):
    tmpCol = MyDataResult.columns[i]
    MyDataResult[tmpCol]=my_client
    

for i in range (len(DataClient)):
    for j in range (len(DataJobbeur)):
      if (DataClient["Localisation du poste"][i] == DataJobbeur["VILLE"][j]):
        MyDataResult.iloc[i,j]+=1
      if (DataJobbeur['Quels sont vos niveaux de disponibilité ? TEXTE'][j] == DataClient['Temps de travail'][i]):
        MyDataResult.iloc[i,j]+=1
      if (DataJobbeur['Niveau de rémunération mensuelle brute souhaitée'][j] >= DataClient['niveau de rémunération'][i]):
        MyDataResult.iloc[i,j]+=1
      if (DataClient["Localisation du poste"][i] == DataJobbeur["Localisation géographique du poste (région, ville)"][j]):
            MyDataResult.iloc[i,j]+=1 
      if (DataClient["Taille entreprise"][i] == DataJobbeur["Quelle taille d'entreprise / organisation TEXTE"][j]):
            MyDataResult.iloc[i,j]+=1                    
      if (DataClient["Comptétences pour le poste 1"][i] == DataJobbeur["Vos compétences 1"][j]):
            MyDataResult.iloc[i,j]+=1
      if (DataClient["Comptétences pour le poste 2"][i] == DataJobbeur["Vos compétences 2"][j]):
            MyDataResult.iloc[i,j]+=1     
      if (DataClient["Comptétences pour le poste 3"][i] == DataJobbeur["Vos compétences 3"][j]):
            MyDataResult.iloc[i,j]+=1         
      if (DataClient["Quels types de contrats pour les embauchés - TEXTE"][i] == DataJobbeur["Quel type de contrat vous intéresse 1"][j]):
            MyDataResult.iloc[i,j]+=1   
      if (DataClient["Quels types de contrats pour les embauchés - TEXTE"][i] == DataJobbeur["Quel type de contrat vous intéresse 2"][j]):
            MyDataResult.iloc[i,j]+=1    
      if (DataClient["Quels types de contrats pour les embauchés - TEXTE"][i] == DataJobbeur["Quel type de contrat vous intéresse 3"][j]):
            MyDataResult.iloc[i,j]+=1    
      if(DataJobbeur["Seriez-vous prêt à déménager pour ce futur job ?"][j]==1):
            MyDataResult.iloc[i,j]+=1
    # if ((DataClient["Mobilité"][i] == 0) and (DataJobbeur["Vous êtes prêt à faire des déplacements professionnels (en % temps)"][j] > str(0))):
     #       MyDataResult.iloc[i,j]-=1      
      if (DataClient["Télétravail ( en %)"][i] == DataJobbeur["Vous souhaitez faire du télétravail (en % temps)"][j]):
            MyDataResult.iloc[i,j]+=1  

          
FindIndexFromJobbeurDataSet = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATAJOBEUR.xlsx",skiprows=[0,1,2,3,4,5])
FindIndexFromJobbeur = FindIndexFromJobbeurDataSet.iloc[:,0]


ListOfPotentialClientByScoring =[0]*len(DataClient)
NameOfJobbeur = input("Enter a name of a Jobbeur :")
ColumnsOfJobberInMyDataset=0
while(NameOfJobbeur != FindIndexFromJobbeur[ColumnsOfJobberInMyDataset]):
        ColumnsOfJobberInMyDataset+=1

for i in range(len(DataClient)):
        ListOfPotentialClientByScoring[i]=MyDataResult.iloc[i,ColumnsOfJobberInMyDataset]      

MaxValueInListOfClient =0
for i in range(len(DataClient)):
        if (ListOfPotentialClientByScoring[i]>MaxValueInListOfClient):
                MaxValueInListOfClient=ListOfPotentialClientByScoring[i]
 
PotentialMatching = [0]*len(DataClient)
j=0
for i in range(len(DataClient)):
        if (ListOfPotentialClientByScoring[i]==MaxValueInListOfClient):
                PotentialMatching[j]=i
                j+=1
Matching = ["Client"]*len(DataClient)

FindNameFromClientDataSet = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATACLIENT.xlsx",skiprows=[0,1,2,3,4,5])
FindNameFromClient= FindNameFromClientDataSet.iloc[:,18]
for i in range(len(DataClient)):
        tmpVar = PotentialMatching[i]
        Matching[i]=FindNameFromClient.iloc[tmpVar]
        
print("Ligne in result data who match the best (high score in columns")
print(PotentialMatching)     
print("All columns of scoring about the Jobbeur (name entered) ")
print(ListOfPotentialClientByScoring)
print("Max value found in the columns ")
print(MaxValueInListOfClient)
print("NAME OF RH in the copagny (client file) ")
print(Matching)                

#print(ListOfPotentialClientByScoring[0])
     #   MyDataResult[j,i]=MyDataResult[j,i].replace(MyDataResult[j,i],1)
       
#print(my_client[1])
#print(len(DataJobbeur))
#print(MyDataResult['Jobbeur 1'][2])
MyDataResult.to_csv("resultData.csv")



#https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-ubuntu-18-04/
