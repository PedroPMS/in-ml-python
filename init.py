from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import tratarDados

tratarDados.tratarDados()

dados = pd.read_csv('./dermatology.data')
dados_treino, dados_teste, resultados_treino, resultados_teste = train_test_split(
    dados.drop('result', axis=1), dados['result'], test_size=0.3)

arvore = DecisionTreeClassifier()
arvore = arvore.fit(dados_treino, resultados_treino)

for feature, importancia in zip(dados.columns, arvore.feature_importances_):
    print("{}: {}".format(feature, importancia))

resultadoPredicao = arvore.predict(dados_teste)
print(metrics.classification_report(resultados_teste, resultadoPredicao))
plot_tree(arvore)
