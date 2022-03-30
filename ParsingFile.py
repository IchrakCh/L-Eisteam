from xml.etree.ElementTree import tostring
import pandas as pd
#import numpy as np
DataJobbeur = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATAJOBEUR.xlsx",skiprows=[0,1,2,3,4,5])
#print(DataJobbeur)
DataClient = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATACLIENT.xlsx",skiprows=[0,1,2,3,4,5,507,506])
#print(DataJobbeur.iloc[[0]])
#print(DataClient.iloc[[0]])

DataClient = DataClient.loc[:, ~DataClient.columns.isin(['Cv obligatoire ','adresse du siège','nom entreprise','Si non, souhaitez-vous vous plus d\'informations ?','Connaissez vous la différence de ces contrats ?','code NAF ', 'siret de l\'entreprise','prénom','nom','un site internet'])]
#DataClient.to_csv('test2.csv')

#print(DataClient.iloc[[0]])
#DataJobbeur.to_csv('test1.csv')
DataJobbeur = DataJobbeur.loc[:, ~DataJobbeur.columns.isin(['NOM','Prénom','CODE POSTAL','Permis PL','Caces 1','Caces 2','Caces 3','Connaissez vous la différence entre ces types de contrats ?','Si non, souhaitez-vous vous plus d\'informations ?','Si vous avez un profil Linkedin ou un e-CV, coller le lien URL :','Si vous avez un site internet, blog ou portfolio coller le lien URL'])]


DataJobbeur = pd.concat([DataJobbeur[col].astype(str).str.lower() for col in DataJobbeur.columns],axis=1)

DataClient = pd.concat([DataClient[col].astype(str).str.lower() for col in DataClient.columns],axis=1)
 

 #Définission de la taille de l'entreprise sous forme de nombres tq:
#1=TPE
#2=PME
#3=ETI
#4=Grand Groupe


##Pour la partie compétence : Faire comme le tp de c++ créer une map par rapport aux données existante et les mettre sous forme de nombres

DataClient['Taille entreprise'] = DataClient['Taille entreprise'].map({
                             'tpe (1 à 10)':'1',
                             'pme (10 à 50)':'2',
                             'eti (50 à 500)':'3',
                             'grand groupe (plus de 500 personnes)':'4',
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
                             'Sous-traitance (Microentreprise)':17,
                             },)                            
  
DataClient.to_csv('test0.csv')
#https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-ubuntu-18-04/
