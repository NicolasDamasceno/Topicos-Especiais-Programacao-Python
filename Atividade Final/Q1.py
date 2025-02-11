import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# Turma 366 - TDS Tarde
# Professor Rogério Batista
# Alunos do Grupo: Nicolas Damasceno e Lyan Kaleu

# Carregando o arquivo CSV
data_set = pd.read_csv('./Atividade Final/heart.csv')

# Separando os dados em variáveis, sendo x e alvo y
x = data_set.drop(columns=["target"]) # Todas as colunas
y = data_set["target"] # Apenas a coluna alvo

# Iremos separar 80% para treinar o modelo e 20% para testa-lo
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Normalizando os dados separados 
escala = StandardScaler()
x_treino_escalado = escala.fit_transform(x_treino)
x_teste_escalado = escala.fit_transform(x_teste)

# Criando e treinando o classificador KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_treino_escalado, y_treino)

# Realizando a previsão do classificadore KNN
y_previsao_kmn = knn.predict(x_teste_escalado)

# Agora calcularemos a sua acurácia (KNN)
acuracia_knn = accuracy_score(y_teste, y_previsao_kmn)
print(f"A acurácia utilizando o KNN: {acuracia_knn*100:.2f}%")

# Como devemos comparar os dois classificadores, iremos também treinar um modelo usando o LinearSVC com os mesmos dados
svc = LinearSVC(max_iter=5000, random_state=42)
svc.fit(x_treino_escalado, y_treino)

# Realizando a previsão com LinearSVC
y_previsao_svc = svc.predict(x_teste_escalado)

# Calculando a sua acurácia
acuracia_svc = accuracy_score(y_teste, y_previsao_svc)
print(f"A acurácia utilizando o LinearSVC: {acuracia_svc*100:.2f}%")

# Comparando as acurácia
if acuracia_svc > acuracia_knn:
    print(f'A acurárioa do Classificador LinearSVC foi de {acuracia_svc*100:.2f}%, com cerca de {(acuracia_svc-acuracia_knn)*100:0.2f}% a mais do KNN')
elif acuracia_knn > acuracia_svc:
    print(f'A acurárioa do Classificador KNN foi de {acuracia_knn*100:.2f}%, com cerca de {(acuracia_knn-acuracia_svc)*100:0.2f}% a mais do LinearSVC')
    print(f'Com isso nota-se que com esse dataset, o classificador mais indicado seria o KNN pois ele possui uma maior acurácia em relação ao LinearSVC')

