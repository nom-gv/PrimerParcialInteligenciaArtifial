import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetHepatitis/main/hepatitis.data')
print(data)

data = pd.DataFrame(data, columns=['Decesos','Edad','Sexo','Esteroides','Antivirales','Fatiga','Malestar','Anorexia','Higado Grande','Firmeza del Higado','Bazo Pulpable','Angioma aracniforme','Ascitis','Bilirrubina','ALP','AST','Albumina','Histologia'])
data

#Importar Librerias para realizar el Ejercicio
import pandas as pd
import numpy as np