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

DataJobbeur = DataJobbeur.loc[:, ~DataJobbeur.columns.isin(['NOM','Prénom','CODE POSTAL','Permis PL','Caces 1','Caces 2','Caces 3','Connaissez vous la différence entre ces types de contrats ?','Si non, souhaitez-vous vous plus d\'informations ?','Si vous avez un profil Linkedin ou un e-CV, coller le lien URL :','Si vous avez un site internet, blog ou portfolio coller le lien URL'])]


DataJobbeur = pd.concat([DataJobbeur[col].astype(str).str.lower() for col in DataJobbeur.columns],axis=1)


DataJobbeur['Quel type de contrat vous intéresse 1'] = DataJobbeur['Quel type de contrat vous intéresse 1'].map({
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

DataJobbeur['Quel type de contrat vous intéresse 2'] = DataJobbeur['Quel type de contrat vous intéresse 2'].map({
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
                             'vdi (vendeur à doicile indépendant)': 4,
                             'alternance, appentissage': 14,
                             },)  

DataJobbeur['Quel type de contrat vous intéresse 3'] = DataJobbeur['Quel type de contrat vous intéresse 3'].map({
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
                             'vdi (vendeur à doicile indépendant)': 4,
                             'alternance, appentissage': 14,
                             },)    


DataJobbeur.to_csv("DataJobbeurParsed.csv")                    

#https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-ubuntu-18-04/
