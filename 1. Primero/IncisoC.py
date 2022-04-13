import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetHepatitis/main/hepatitis.data')

data = pd.DataFrame(data, columns=['Decesos','Edad','Sexo','Esteroides','Antivirales','Fatiga','Malestar','Anorexia','Higado Grande','Firmeza del Higado','Bazo Pulpable','Angioma aracniforme','Ascitis','Bilirrubina','ALP','AST','Albumina','Histologia'])
print(data)

#GRAFICOS PARA REALIZAR EL EJERCICIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets


Filtro=data[data['Bilirrubina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Bilirrubina']=pd.to_numeric(Data_E['Bilirrubina'])

sns.set(style="ticks")
#Obtenemos los niveles de Bilirrubina de cada sexo
sns.lmplot(x='Bilirrubina', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Bilirrubina de los Decesos
sns.lmplot(x='Bilirrubina', y='Edad', col='Decesos', hue='Decesos', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Bilirrubina de personas que utilizan Antivirales
sns.lmplot(x='Bilirrubina', y='Edad', col='Antivirales', hue='Antivirales', data=Data_E,  height=6, ci=None, palette="muted");

#Realizamos la matriz de disperción de la edad y los niveles de birrubina
Data_Bil = pd.DataFrame(Data_E, columns=['Sexo', 'Edad', 'Bilirrubina'])

sns.pairplot(Data_Bil, hue='Sexo')  
plt.show()


Filtro=data[data['ALP']>='?'].index
Data_E=data.drop(Filtro)
Data_E['ALP']=pd.to_numeric(Data_E['ALP'])
#Obtenemos los niveles de Fosfatasa Alcalina de cada sexo
sns.lmplot(x='ALP', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Fosfatasa Alcalina de los Decesos
sns.lmplot(x='ALP', y='Edad', col='Decesos', hue='Decesos', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Fosfatasa Alcalina de personas que utilizan Antivirales
sns.lmplot(x='ALP', y='Edad', col='Antivirales', hue='Antivirales', data=Data_E,  height=6, ci=None, palette="muted");


Filtro=data[data['AST']>='?'].index
Data_E=data.drop(Filtro)
Data_E['AST']=pd.to_numeric(Data_E['AST'])
#Obtenemos los niveles de Aspartato transaminasa de cada sexo
sns.lmplot(x='AST', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Aspartato transaminasa de los Decesos
sns.lmplot(x='AST', y='Edad', col='Decesos', hue='Decesos', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Aspartato transaminasa de personas que utilizan Antivirales
sns.lmplot(x='AST', y='Edad', col='Antivirales', hue='Antivirales', data=Data_E,  height=6, ci=None, palette="muted");



Filtro=data[data['Albumina']>='?'].index
Data_E=data.drop(Filtro)
Data_E['Albumina']=pd.to_numeric(Data_E['Albumina'])
#Obtenemos los niveles de Albumina de cada sexo
sns.lmplot(x='Albumina', y='Edad', col='Sexo', hue='Sexo', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Albumina de los Decesos
sns.lmplot(x='Albumina', y='Edad', col='Decesos', hue='Decesos', data=Data_E,  height=6, ci=None, palette="muted");
#Obtenemos los niveles de Albumina de personas que utilizan Antivirales
sns.lmplot(x='Albumina', y='Edad', col='Antivirales', hue='Antivirales', data=Data_E,  height=6, ci=None, palette="muted");


#REALIZAMOS LA EXTRACCIÓN DE LOS DATOS DE DECESOS PARA CADA SEXO POR RANGO DE EDAD
grupo_edad = pd.cut(data['Edad'], bins=[0, 20, 40, 60, np.inf])
grupo_edad

data2 = data
data2.Sexo = data2.Sexo.replace({1: "Masculino", 2: "Femenino"})
data2.Decesos = data2.Decesos.replace({1: "Muerto", 2: "Vivo"})

dataC = pd.crosstab(grupo_edad, [data2['Sexo'], data['Decesos']])
print(dataC)
#Obtenemos la gráfica de linea para el rango de edad y los datos de muertes y vidas de los sexos
dataC.plot(kind='line', figsize=(10, 5))
#Obtenemos la gráfica de barras para el rango de edad y los datos de muertes y vidas de los sexos
dataC.plot(kind='barh', figsize=(10, 6))
#Obtenemos la gráfica de histograma para el rango de edad y los datos de muertes y vidas de los sexos
dataC.plot(kind='hist', figsize=(10, 5))
#Obtenemos la gráfica de area para el rango de edad y los datos de muertes y vidas de los sexos
dataC.plot(kind='area', figsize=(10, 5))
#Obtenemos las gráficas de pastel para los rangos de edad para los datos de muertes y vidas de ambos sexos
dataC.plot(kind='pie', subplots=True, figsize=(20,20), autopct='%1.1f%%')
#Obtenemos las gráficas de barras para los rangos de edad para los datos de muertes y vidas de ambos sexos
dataC.plot(subplots=True, figsize=(6,10), kind='bar');

dataC = pd.crosstab(grupo_edad, [data2['Sexo'], data['Decesos']]).stack().stack().reset_index(name='Cantidad')
print(dataC)