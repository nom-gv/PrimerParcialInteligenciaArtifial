import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/nom-gv/DatasetHepatitis/main/hepatitis.data')
print(data)

data = pd.DataFrame(data, columns=['Decesos','Edad','Sexo','Esteroides','Antivirales','Fatiga','Malestar','Anorexia','Higado Grande','Firmeza del Higado','Bazo Pulpable','Angioma aracniforme','Ascitis','Bilirrubina','ALP','AST','Albumina','Histologia'])
data

#UNCIONES PARA REALIZAR LOS EJERCICIOS
#Para valores vacios
def isnan(num):
    return num != num

#Para Cuatiles:
def cuartil(columna,nc):
    valores = pd.to_numeric(data[columna],errors='coerce').to_list()
    val = [x for x in valores if isnan(x) == False]
    val.sort()
    
    #Posicion del cuartil 1
    P1 = int((nc*len(val))/4)
    
    if(len(val)%2 == 0):
        Q1 = (val[P1] + val[P1+1])/2
    else:
        Q1 = float(val[P1])
    return Q1

#Para Percentiles
def percentil(columna,nc):
    valores = pd.to_numeric(data[columna],errors='coerce').to_list()
    val = [x for x in valores if isnan(x) == False]
    val.sort()
    
    #Posicion del cuartil 1
    P1 = int((nc*len(val))/100)
    
    if(len(val)%2 == 0):
        Q1 = (val[P1] + val[P1+1])/2
    else:
        Q1 = float(val[P1])
    return Q1



#CALCULO DEL PRIMER CUARTIL DE LOS DATOS
print("\n\nCALCULO DEL PRIMER CUARTIL DE TODAS LAS COLUMNAS\n")


#Obtenemos que los decesos son menores al 25% de los casos detectados de hepatitis
print("Calculo del primer Cuartil de decesos: ", cuartil('Decesos',1))

#Se btuvo que hasta el 25% de personas con hepatitis se encuentran entre las edades de 7 a 32 años
print("Calculo del primer Cuartil de edades: ", cuartil('Edad',1))

#Se obtuvo que hasta el 25% de personas con hepatitis son hombres
print("Calculo del primer Cuartil del sexo del paciente: ", cuartil('Sexo',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no utilizaron esteroides
print("Calculo del primer Cuartil de pacientes que utilizan Esteroides: ", cuartil('Esteroides',1))

#Obtenemos que personas que no utilizaron antivirales son menores a 25% en los casos detectados de hepatitis
print("Calculo del primer Cuartil de pacientes que utilizan Antivirales: ", cuartil('Antivirales',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentaron fatiga
print("Calculo del primer Cuartil de Fatiga en pacientes: ", cuartil('Fatiga',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentaron malestar
print("Calculo del primer Cuartil de Malestar en pacientes: ", cuartil('Malestar',1))

#Obtenemos que, de los datos obtenidos, las personas que no tienen anorexia son menores a 25% en los casos detectados de hepatitis
print("Calculo del primer Cuartil de anorexia en pacientes: ", cuartil('Anorexia',1))

#Obtenemos que, de los datos obtenidos, las personas que no tienen el higado grande son menores a 25% en los casos detectados de hepatitis
print("Calculo del primer Cuartil de Higado Grande en pacientes: ", cuartil('Higado Grande',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no tienen firmeza del higado
print("Calculo del primer Cuartil de la Firmeza del Higado en los pacientes: ", cuartil('Firmeza del Higado',1))

#Obtenemos que, de los datos obtenidos, las personas que no tienen el bazo pulpable son menores a 25% en los casos detectados de hepatitis
print("Calculo del primer Cuartil de Bazo pulpable en pacientes: ", cuartil('Bazo Pulpable',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no tienen Angioma Aracniforme
print("Calculo del primer Cuartil de Angioma aracniforme en pacientes: ", cuartil('Angioma aracniforme',1))

#Obtenemos que, de los datos obtenidos, las personas que no tienen Ascitis son menores a 25% en los casos detectados de hepatitis
print("Calculo del primer Cuartil de Ascitis en pacientes: ", cuartil('Ascitis',1))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Bilirrubina entre 0.3 y 0.7 se encuentran entre el 25% los casos detectados de hepatitis
print("Calculo del primer Cuartil de Niveles Bilirrubina en pacientes: ", cuartil('Bilirrubina',1))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Fosfatasa Alcalina entre 30 y 74 se encuentran entre el 25% los casos detectados de hepatitis
print("Calculo del primer Cuartil de Niveles Fosfatasa alcalina en pacientes: ", cuartil('ALP',1))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Aspartato Transaminasa entre 13 y 31 se encuentran entre el 25% los casos detectados de hepatitis
print("Calculo del primer Cuartil de Niveles Aspartato transaminasa en pacientes: ", cuartil('AST',1))

#Obtenemos que, de los datos obtenidos, las personas que tienen valores de Albumina entre 2.1 y 3.4 se encuentran entre el 25% los casos detectados de hepatitis
print("Calculo del primer Cuartil de Niveles Aspartato transaminasa en pacientes: ", cuartil('Albumina',1))

#Se obtuvo que, de los datos obtenidos, hasta el 25% de personas con hepatitis no presentan Histologia
print("Calculo del primer Cuartil de Histologia en pacientes: ", cuartil('Histologia',1))



#CALCULO DEL PERCENTIL 50 DE LOS DATOS
print("\n\nCALCULO DEL PERCENTIL 50 DE TODAS LAS COLUMNAS\n")


#Obtenemos que los decesos son menores al 50% de los casos detectados de hepatitis
print("Calculo del Percentil 50 de decesos: ", percentil('Decesos',50))

#Se obtuvo que hasta el 50% de personas con hepatitis se encuentran entre las edades de 7 a 39 años
print("Calculo del Percentil 50 de edades: ", percentil('Edad',50))

#Se obtuvo que hasta el 50% de personas con hepatitis son hombres
print("Calculo del Percentil 50 del sexo del paciente: ", percentil('Sexo',50))

#Obtenemos que personas que no utilizaron esteroides son menores al 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de pacientes que utilizan Esteroides: ", percentil('Esteroides',50))

#Obtenemos que personas que no utilizaron antivirales son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de pacientes que utilizan Antivirales: ", percentil('Antivirales',50))

#Se obtuvo que, de los datos obtenidos, hasta el 50% de personas con hepatitis no presentaron fatiga
print("Calculo del Percentil 50 de Fatiga en pacientes: ", percentil('Fatiga',50))

#Obtenemos que personas que no presentaron malestar son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de Malestar en pacientes: ", percentil('Malestar',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen anorexia son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de anorexia en pacientes: ", percentil('Anorexia',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen el higado grande son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de Higado Grande en pacientes: ", percentil('Higado Grande',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen Firmeza del higado son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de la Firmeza del Higado en los pacientes: ", percentil('Firmeza del Higado',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen el bazo pulpable son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de Bazo pulpable en pacientes: ", percentil('Bazo Pulpable',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen el Angioma Aracniforme son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de Angioma aracniforme en pacientes: ", percentil('Angioma aracniforme',50))

#Obtenemos que, de los datos obtenidos, las personas que no tienen Ascitis son menores a 50% en los casos detectados de hepatitis
print("Calculo del Percentil 50 de Ascitis en pacientes: ", percentil('Ascitis',50))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Bilirrubina entre 0.3 y 1.0 se encuentran entre el 50% los casos detectados de hepatitis
print("Calculo del Percentil 50 de Niveles Bilirrubina en pacientes: ", percentil('Bilirrubina',50))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Fosfatasa Alcalina entre 30 y 85 se encuentran entre el 50% los casos detectados de hepatitis
print("Calculo del Percentil 50 de Niveles Fosfatasa alcalina en pacientes: ", percentil('ALP',50))

#Obtenemos que, de los datos obtenidos, las personas que tienen niveles de Aspartato Transaminasa entre 13 y 58 se encuentran entre el 50% los casos detectados de hepatitis
print("Calculo del Percentil 50 de Niveles Aspartato transaminasa en pacientes: ", percentil('AST',50))

#Obtenemos que, de los datos obtenidos, las personas que tienen valores de Albumina entre 2.1 y 4.0 se encuentran entre el 50% los casos detectados de hepatitis
print("Calculo del Percentil 50 de Niveles Aspartato transaminasa en pacientes: ", percentil('Albumina',50))

#Se obtuvo que, de los datos obtenidos, hasta el 50% de personas con hepatitis no presentan Histologia
print("Calculo del Percentil  de Histologia en pacientes: ", percentil('Histologia',50))
