### Mis Funciones - Curso Ciencia de Datos 2024

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate

# verifique la estructura del set de datos
def check_df(dataframe,_flag, data, Encabezado):
    if _flag == 1:
      print(Encabezado)
      print(dataframe.data)
      print("*"*120)
      print("*"*120)


descriptores= [ [shape,"Shape: Dimención del dataframe"]
               ,[head(),"Head: Las primeras 5 filas del dataframe"]
               ,[tail(),"Tail: Las últimas 5 filas del dataframe"]
               ,[info(),"Info:\n"]
               ,[describe(),"Describe:\n"]
               ,[columns,"Columnas:\n"]
               ,[dtypes,"Date Type:\n"]
               ,[isnull().sum(),"Null Values:\n"]
               ,[nunique(),"Unique Values:\n"]]
               
def verificar_df(data,flags=None):
    # Si no se proporcionan flags, usar [1, 1, 1, 1, 1, 1, 1, 1, 1] por defecto
    if flags is None:
        flags = [1] * 9  # Crea una lista de 9 elementos con valor 1
    
    for i, flag in enumerate(flags):
        check_df(data,flag, descriptores[i][0], descriptores[i][1])
    
    
def metricas(conf_matrix):
  # Calculamos las tasas de falsos positivos y negativos
  FP = conf_matrix[0,1]
  FN = conf_matrix[1,0]
  TN = conf_matrix[0,0]
  TP = conf_matrix[1,1]
  FPR = FP / (FP + TN)
  FNR = FN / (FN + TP)

  accuracy = (TP + TN) / (TP + TN + FP + FN)
  precision = TP / (TP + FP)
  recall = TP / (TP + FN)
  specificity = TN / (TN + FP)
  f1 = 2 * (precision * recall) / (precision + recall)

  # Mostramos los resultados
  print("Métricas de evaluación:")
  print(f"Accuracy - Exactitud\t\t: {accuracy:.4f}")
  print(f"Precision - Precisión\t\t: {precision:.4f}")
  print(f"Recall- Sensibilidad\t\t: {recall:.4f}")
  print(f"Specificity - Especificidad\t: {specificity:.4f}")
  print(f"F1-score\t\t\t: {f1:.4f}")
  print("\nMatriz de Confusión:")
  print("\n-------")
  print("|TN|FP|")
  print("|FN|TP|")
  print("-------\n")
  print(conf_matrix)
  print(tabulate(conf_matrix, headers='keys', tablefmt='fancy_grid'))
  print("\nTasas de Falsos Positivos y Negativos:")
  print(f"Tasa de Falsos Positivos (FPR): {FPR:.4f}")
  print(f"Tasa de Falsos Negativos (FNR): {FNR:.4f}")
