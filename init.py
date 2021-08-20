from sklearn.tree import DecisionTreeClassifier
import csv
import pandas as pd
import tratarDados

tratarDados.tratarDados()

dados = pd.read_csv('./dermatology.data')

dados.head()
dados.info()