import pandas as pd
DataJobbeur = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATAJOBEUR.xlsx",skiprows=[0,1,2,3,4,5])
#print(DataJobbeur)
DataClient = pd.read_excel(r"/home/hadrien//ProjetTatami/L-Eisteam/DATACLIENT.xlsx",skiprows=[0,1,2,3,4,507,506])
#print(DataJobbeur.iloc[[0]])
#print(DataClient.iloc[[0]])