import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetHepatitis/main/hepatitis.data')
print(data)

data = pd.DataFrame(data, columns=['Decesos','Edad','Sexo','Esteroides','Antivirales','Fatiga','Malestar','Anorexia','Higado Grande','Firmeza del Higado','Bazo Pulpable','Angioma aracniforme','Ascitis','Bilirrubina','ALP','AST','Albumina','Histologia'])
data

#Importar Librerias para realizar el Ejercicio
import pandas as pd
import numpy as np

#CALCULO DEL PRIMER CUARTIL DE LOS DATOS
print("\n\nCALCULO DEL PRIMER CUARTIL DE TODAS LAS COLUMNAS\n")


#Obtenemos que los decesos son menores al 25% de los casos detectados de hepatitis
Q1 = data['Decesos'].quantile(.25)
print("Calculo del primer Cuartil de decesos: ",Q1)

#Se obtuvo que hasta el 25% de personas con hepatitis se encuentran entre las edades de 7 a 32 años
Q1 = data['Edad'].quantile(.25)
print("Calculo del primer Cuartil de edades: ",Q1)

#Se obtuvo que hasta el 25% de personas con hepatitis son hombres
Q1 = data['Sexo'].quantile(.25)
print("Calculo del primer Cuartil del sexo del paciente: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no utilizaron esteroides
Filtro=data[data["Esteroides"]>='?'].index
Data_E=data.drop(Filtro)
Data_E['Esteroides']=pd.to_numeric(Data_E["Esteroides"])

Q1 = Data_E['Esteroides'].quantile(.25)
print("Calculo del primer Cuartil de pacientes que utilizan Esteroides: ",Q1)

#Obtenemos que personas que no utilizaron antivirales son menores a 25% en los casos detectados de hepatitis
Q1 = data['Antivirales'].quantile(.25)
print("Calculo del primer Cuartil de pacientes que utilizan Antivirales: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentaron fatiga
Filtro=data[data['Fatiga']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Fatiga']=pd.to_numeric(Data_E['Fatiga'])

Q1 = Data_E['Fatiga'].quantile(.25)
print("Calculo del primer Cuartil de Fatiga en pacientes: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentaron malestar
Filtro=data[data['Malestar']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Malestar']=pd.to_numeric(Data_E['Malestar'])

Q1 = Data_E['Malestar'].quantile(.25)
print("Calculo del primer Cuartil de Malestar en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen anorexia son menores a 25% en los casos detectados de hepatitis
Filtro=data[data['Anorexia']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Anorexia']=pd.to_numeric(Data_E['Anorexia'])

Q1 = Data_E['Anorexia'].quantile(.25)
print("Calculo del primer Cuartil de anorexia en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen el higado grande son menores a 25% en los casos detectados de hepatitis
Filtro=data[data['Higado Grande']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Higado Grande']=pd.to_numeric(Data_E['Higado Grande'])

Q1 = Data_E['Higado Grande'].quantile(.25)
print("Calculo del primer Cuartil de Higado Grande en pacientes: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no tienen firmeza del higado
Filtro=data[data['Firmeza del Higado']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Firmeza del Higado']=pd.to_numeric(Data_E['Firmeza del Higado'])

Q1 = Data_E['Firmeza del Higado'].quantile(.25)
print("Calculo del primer Cuartil de la Firmeza del Higado en los pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen el bazo pulpable son menores a 25% en los casos detectados de hepatitis
Filtro=data[data['Bazo Pulpable']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Bazo Pulpable']=pd.to_numeric(Data_E['Bazo Pulpable'])

Q1 = Data_E['Bazo Pulpable'].quantile(.25)
print("Calculo del primer Cuartil de Bazo pulpable en pacientes: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no tienen Angioma Aracniforme
Filtro=data[data['Angioma aracniforme']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Angioma aracniforme']=pd.to_numeric(Data_E['Angioma aracniforme'])

Q1 = Data_E['Angioma aracniforme'].quantile(.25)
print("Calculo del primer Cuartil de Angioma aracniforme en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen Ascitis son menores a 25% en los casos detectados de hepatitis
Filtro=data[data['Ascitis']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Ascitis']=pd.to_numeric(Data_E['Ascitis'])

Q1 = Data_E['Ascitis'].quantile(.25)
print("Calculo del primer Cuartil de Ascitis en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Bilirrubina entre 0.3 y 0.7 se encuentran entre el 25% los casos detectados de hepatitis
Filtro=data[data['Bilirrubina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Bilirrubina']=pd.to_numeric(Data_E['Bilirrubina'])

Q1 = Data_E['Bilirrubina'].quantile(.25)
print("Calculo del primer Cuartil de Niveles Bilirrubina en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Fosfatasa Alcalina entre 30 y 74 se encuentran entre el 25% los casos detectados de hepatitis
Filtro=data[data['ALP']>='?'].index
Data_E=data.drop(Filtro)
Data_E['ALP']=pd.to_numeric(Data_E['ALP'])

Q1 = Data_E['ALP'].quantile(.25)
print("Calculo del primer Cuartil de Niveles Fosfatasa alcalina en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Aspartato Transaminasa entre 13 y 31 se encuentran entre el 25% los casos detectados de hepatitis
Filtro=data[data['AST']>='?'].index
Data_E=data.drop(Filtro)
Data_E['AST']=pd.to_numeric(Data_E['AST'])

Q1 = Data_E['AST'].quantile(.25)
print("Calculo del primer Cuartil de Niveles Aspartato transaminasa en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen valores de Albumina entre 2.1 y 3.4 se encuentran entre el 25% los casos detectados de hepatitis
Filtro=data[data['Albumina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Albumina']=pd.to_numeric(Data_E['Albumina'])

Q1 = Data_E['Albumina'].quantile(.25)
print("Calculo del primer Cuartil de Niveles Aspartato transaminasa en pacientes: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentan Histologia
Filtro=data[data['Histologia']=='?'].index
Data_E=data.drop(Filtro)
Data_E['Histologia']=pd.to_numeric(Data_E['Histologia'])

Q1 = Data_E['Histologia'].quantile(.25)
print("Calculo del primer Cuartil de Histologia en pacientes: ",Q1)



#CALCULO DEL PERCENTIL 50 DE LOS DATOS
print("\n\nCALCULO DEL PERCENTIL 50 DE TODAS LAS COLUMNAS\n")

#Obtenemos que los decesos son menores al 50% de los casos detectados de hepatitis
Q1 = data['Decesos'].quantile(.50)
print("Calculo del Percentil 50 de decesos: ",Q1)

#Se obtuvo que hasta el 50% de personas con hepatitis se encuentran entre las edades de 7 a 39 años
Q1 = data['Edad'].quantile(.50)
print("Calculo del Percentil 50 de edades: ",Q1)

#Se obtuvo que hasta el 50% de personas con hepatitis son hombres
Q1 = data['Sexo'].quantile(.50)
print("Calculo del Percentil 50 del sexo del paciente: ",Q1)

#Obtenemos que personas que no utilizaron esteroides son menores al 50% en los casos detectados de hepatitis 
Filtro=data[data["Esteroides"]>='?'].index
Data_E=data.drop(Filtro)
Data_E['Esteroides']=pd.to_numeric(Data_E["Esteroides"])

Q1 = Data_E['Esteroides'].quantile(.50)
print("Calculo del Percentil 50 de pacientes que utilizan Esteroides: ",Q1)

#Obtenemos que personas que no utilizaron antivirales son menores a 50% en los casos detectados de hepatitis
Q1 = data['Antivirales'].quantile(.50)
print("Calculo del Percentil 50 de pacientes que utilizan Antivirales: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 50% de personas con hepatitis no presentaron fatiga
Filtro=data[data['Fatiga']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Fatiga']=pd.to_numeric(Data_E['Fatiga'])

Q1 = Data_E['Fatiga'].quantile(.50)
print("Calculo del Percentil 50 de Fatiga en pacientes: ",Q1)

#Obtenemos que personas que no presentaron malestar son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Malestar']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Malestar']=pd.to_numeric(Data_E['Malestar'])

Q1 = Data_E['Malestar'].quantile(.50)
print("Calculo del Percentil 50 de Malestar en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen anorexia son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Anorexia']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Anorexia']=pd.to_numeric(Data_E['Anorexia'])

Q1 = Data_E['Anorexia'].quantile(.50)
print("Calculo del Percentil 50 de anorexia en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen el higado grande son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Higado Grande']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Higado Grande']=pd.to_numeric(Data_E['Higado Grande'])

Q1 = Data_E['Higado Grande'].quantile(.25)
print("Calculo del Percentil 50 de Higado Grande en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen Firmeza del higado son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Firmeza del Higado']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Firmeza del Higado']=pd.to_numeric(Data_E['Firmeza del Higado'])

Q1 = Data_E['Firmeza del Higado'].quantile(.50)
print("Calculo del Percentil 50 de la Firmeza del Higado en los pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen el bazo pulpable son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Bazo Pulpable']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Bazo Pulpable']=pd.to_numeric(Data_E['Bazo Pulpable'])

Q1 = Data_E['Bazo Pulpable'].quantile(.50)
print("Calculo del Percentil 50 de Bazo pulpable en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen el Angioma Aracniforme son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Angioma aracniforme']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Angioma aracniforme']=pd.to_numeric(Data_E['Angioma aracniforme'])

Q1 = Data_E['Angioma aracniforme'].quantile(.50)
print("Calculo del Percentil 50 de Angioma aracniforme en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que no tienen Ascitis son menores a 50% en los casos detectados de hepatitis
Filtro=data[data['Ascitis']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Ascitis']=pd.to_numeric(Data_E['Ascitis'])

Q1 = Data_E['Ascitis'].quantile(.50)
print("Calculo del Percentil 50 de Ascitis en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Bilirrubina entre 0.3 y 1.0 se encuentran entre el 50% los casos detectados de hepatitis
Filtro=data[data['Bilirrubina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Bilirrubina']=pd.to_numeric(Data_E['Bilirrubina'])

Q1 = Data_E['Bilirrubina'].quantile(.50)
print("Calculo del Percentil 50 de Niveles Bilirrubina en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Fosfatasa Alcalina entre 30 y 85 se encuentran entre el 50% los casos detectados de hepatitis
Filtro=data[data['ALP']>='?'].index
Data_E=data.drop(Filtro)
Data_E['ALP']=pd.to_numeric(Data_E['ALP'])

Q1 = Data_E['ALP'].quantile(.50)
print("Calculo del Percentil 50 de Niveles Fosfatasa alcalina en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Aspartato Transaminasa entre 13 y 58 se encuentran entre el 50% los casos detectados de hepatitis
Filtro=data[data['AST']>='?'].index
Data_E=data.drop(Filtro)
Data_E['AST']=pd.to_numeric(Data_E['AST'])

Q1 = Data_E['AST'].quantile(.50)
print("Calculo del Percentil 50 de Niveles Aspartato transaminasa en pacientes: ",Q1)

#Obtenemos que, de los datos obtenidos, las personas que tienen valores de Albumina entre 2.1 y 4.0 se encuentran entre el 50% los casos detectados de hepatitis
Filtro=data[data['Albumina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Albumina']=pd.to_numeric(Data_E['Albumina'])

Q1 = Data_E['Albumina'].quantile(.50)
print("Calculo del Percentil 50 de Niveles Aspartato transaminasa en pacientes: ",Q1)

#Se obtuvo que, de los datos obtenidos, hasta el 50% de personas con hepatitis no presentan Histologia
Filtro=data[data['Histologia']=='?'].index
Data_E=data.drop(Filtro)
Data_E['Histologia']=pd.to_numeric(Data_E['Histologia'])

Q1 = Data_E['Histologia'].quantile(.50)
print("Calculo del Percentil  de Histologia en pacientes: ",Q1)