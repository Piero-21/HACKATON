import pandas as pd
import numpy as np
from sklearn import linear_model

training_dataset = pd.read_csv('area23.csv', header = 0)
training_dataset2 = pd.read_csv('valor.csv')

original_headers = list(training_dataset.columns.values)

regression_model = linear_model.LinearRegression()
print ("Training model...")
# entrenamiento del modelo
regression_model.fit(training_dataset, training_dataset2.valor) 
print ("Model trained.")

input_area = float(input("Enter area: "))
input_ln = float(input("Enter longitud: "))
input_lt = float(input("Enter latitud: "))
input_ct = int(input("Enter categoria: "))
input_ac = float(input("Enter area_construcción: "))
ar = [input_lt, input_ln, input_ct, input_area, input_ac]
proped_price = regression_model.predict([ar])
print ("Proped price:", round(proped_price[0], 2))