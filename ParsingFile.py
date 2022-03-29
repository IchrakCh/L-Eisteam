import pandas as pd
DataJobbeur = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATAJOBEUR.xlsx",skiprows=[0,1,2,3,4,5])
#print(DataJobbeur)
DataClient = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATACLIENT.xlsx",skiprows=[0,1,2,3,4,5,507,506])
#print(DataJobbeur.iloc[[0]])
#print(DataClient.iloc[[0]])

DataClient = DataClient.loc[:, ~DataClient.columns.isin(['code NAF ', 'siret de l\'entreprise','prénom','nom','un site internet'])]
#DataClient.to_csv('test2.csv')

#print(DataClient.iloc[[0]])
#DataJobbeur.to_csv('test1.csv')
DataJobbeur = DataJobbeur.loc[:, ~DataJobbeur.columns.isin(['NOM','Prénom','CODE POSTAL','Permis PL','Caces 1','Caces 2','Caces 3','Connaissez vous la différence entre ces types de contrats ?','Si non, souhaitez-vous vous plus d\'informations ?','Si vous avez un profil Linkedin ou un e-CV, coller le lien URL :','Si vous avez un site internet, blog ou portfolio coller le lien URL'])]


DataJobbeur = pd.concat([DataJobbeur[col].astype(str).str.lower() for col in DataJobbeur.columns],axis=1)

DataClient = pd.concat([DataClient[col].astype(str).str.lower() for col in DataClient.columns],axis=1)
DataClient.to_csv('test1.csv')
#https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-ubuntu-18-04/
