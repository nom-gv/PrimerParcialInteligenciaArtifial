import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetHepatitis/main/hepatitis.data')

data = pd.DataFrame(data, columns=['Decesos','Edad','Sexo','Esteroides','Antivirales','Fatiga','Malestar','Anorexia','Higado Grande','Firmeza del Higado','Bazo Pulpable','Angioma aracniforme','Ascitis','Bilirrubina','ALP','AST','Albumina','Histologia'])


data['Esteroides'] = pd.to_numeric(data['Esteroides'],errors='coerce').to_list()
data['Fatiga'] = pd.to_numeric(data['Fatiga'],errors='coerce').to_list()
data['Malestar'] = pd.to_numeric(data['Malestar'],errors='coerce').to_list()
data['Anorexia'] = pd.to_numeric(data['Anorexia'],errors='coerce').to_list()
data['Higado Grande'] = pd.to_numeric(data['Higado Grande'],errors='coerce').to_list()
data['Firmeza del Higado'] = pd.to_numeric(data['Firmeza del Higado'],errors='coerce').to_list()
data['Bazo Pulpable'] = pd.to_numeric(data['Bazo Pulpable'],errors='coerce').to_list()
data['Higado Grande'] = pd.to_numeric(data['Higado Grande'],errors='coerce').to_list()
data['Angioma aracniforme'] = pd.to_numeric(data['Angioma aracniforme'],errors='coerce').to_list()
data['Ascitis'] = pd.to_numeric(data['Ascitis'],errors='coerce').to_list()
data['Bilirrubina'] = pd.to_numeric(data['Bilirrubina'],errors='coerce').to_list()
data['ALP'] = pd.to_numeric(data['ALP'],errors='coerce').to_list()
data['AST'] = pd.to_numeric(data['AST'],errors='coerce').to_list()
data['Albumina'] = pd.to_numeric(data['Albumina'],errors='coerce').to_list()
data['Histologia'] = pd.to_numeric(data['Histologia'],errors='coerce').to_list()

print(data)
#Reemplazamos los valores perdidos con la media de cada columna
import numpy as np
from sklearn.impute import SimpleImputer
X = data.iloc[:, 12:17].values
y = data.iloc[:, 0].values

print(X)

imputer = SimpleImputer(missing_values = np.nan, strategy="most_frequent")
imputer = imputer.fit(X[:,0:5])
X[:, 0:5] = imputer.transform(X[:,0:5])


print(X)
print(y)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)



import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 


dot_data = tree.export_graphviz(clf, out_file=None, 
                     feature_names=['Ascitis','Bilirrubina','ALP','AST','Albumina'],  
                     class_names=["Muerto","Vivo"],  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("Hepatitis") 