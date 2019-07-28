#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Autor: Otávio A M Guerra

"""
Script que prepara o conjunto de dados que será utilizado
para treinamento e validação dos algoritmos.
---------------------------------------------------------------------------------------
> Procedimento:
    
    1) Baixar e descompactar o Dataset disponibilizado no link:
    https://www.kaggle.com/paultimothymooney/breast-histopathology-images
                
    2) Executar este script alterando a variavel path_dataset
    com o caminho da pasta baixada.
----------------------------------------------------------------------------------------
> Saída: 3 arquivos CSV contendo Conjunto de Treino, Validacao e Teste
        os conjuntos de validacao e teste possui 10mil imagens sendo 5000 pertencentes
        a cada classe. O conjunto de treino consiste nas imagens restantes.

"""

# Importacao das bibliotecas necessarias
import numpy as np
import random
import cv2
random.seed(0) # Seed para garantir reprodutibilidade 
from glob import glob
import fnmatch

# Lê os caminhos de cada imagem da pasta do dataset para um array:
imagePaths = glob('/home/otavio/Desktop/Faculdade/TCC/IDC_regular_ps50_idx5/**/*.png', recursive=True)
random.shuffle(imagePaths)
print("Numero de imagens {}".format(len(imagePaths)))

# Define 2 arrays que guardam os caminhos das imagens de cada classe:
patternZero = '*class0.png'
patternOne = '*class1.png'
classZero = fnmatch.filter(imagePaths, patternZero)
classOne = fnmatch.filter(imagePaths, patternOne)
print("IDC(-): ",len(classZero),'\n')
print("IDC(+): ",len(classOne),'\n')

# Split de Treino e Validação
np.random.seed(0) # Seed para garantir Reprodutibilidade

# Variaveis que guardam os caminhos dos arquivos:
all_images = set(imagePaths)
validationPaths = []
testPaths = []
trainPaths = set()

# Constroi conjunto de validacao escolhendo aleatoriamente 10000 imagens
# 5000 de classe positiva e 5000 de classe negativa
validation_0 = list(np.random.choice(classZero,5000,replace=False))
validation_1 = list(np.random.choice(classOne,5000,replace=False))
    
for x in validation_0: validationPaths.append(str(x)) 
for y in validation_1: validationPaths.append(str(y))

valPaths = set(validationPaths)

# Constroi conjunto de teste escolhendo aleatoriamente 10000 imagens
# 5000 de classe positiva e 5000 de classe negativa
test_0 = list(np.random.choice(list(set(classZero).difference(validationPaths)),5000,replace=False))
test_1 = list(np.random.choice(list(set(classOne).difference(validationPaths)),5000,replace=False))
    
for x in test_0: testPaths.append(str(x)) 
for y in test_1: testPaths.append(str(y))

testPaths = set(testPaths)

# Conjunto de treino consiste em todas as imagens que nao estao no
# conjunto de validacao e nem no conjunto de teste

trainPaths = all_images.difference(valPaths.union(testPaths))

# Prints de contagens
print("Conjunto de treino e validacao são disjuntos? {}\n".format(trainPaths.isdisjoint(valPaths)))
print("Conjunto de treino e teste são disjuntos? {}\n".format(trainPaths.isdisjoint(testPaths)))
print("Conjunto de validação e teste são disjuntos? {}\n".format(valPaths.isdisjoint(testPaths)))
print('\n')
print('--------------------------------------------------------------')
print("Tamanho do conjunto de Treino: {}\n".format(len(trainPaths)))
print("Tamanho do conjunto de Validacao: {}\n".format(len(valPaths)))
print("Tamanho do conjunto de Teste: {}\n".format(len(testPaths)))

classZero_train = fnmatch.filter(trainPaths, patternZero)
classOne_train = fnmatch.filter(trainPaths, patternOne)
print("IDC(-) Treino: ",len(classZero_train),'\n')
print("IDC(+) Treino: ",len(classOne_train),'\n')

print('--------------------------------------------------------------')
classZero_val = fnmatch.filter(valPaths, patternZero)
classOne_val = fnmatch.filter(valPaths, patternOne)
print("IDC(-) Validacao: ",len(classZero_val),'\n')
print("IDC(+) Validacao: ",len(classOne_val),'\n')

print('--------------------------------------------------------------')
classZero_test = fnmatch.filter(testPaths, patternZero)
classOne_test = fnmatch.filter(testPaths, patternOne)
print("IDC(-) Teste: ",len(classZero_test),'\n')
print("IDC(+) Teste: ",len(classOne_test),'\n')

# Definicao dos datasets
datasets = [
	("Treino", trainPaths, "IDC_training.csv"),
	("Validacao", valPaths, "IDC_validation.csv"),
    ("Teste", testPaths, "IDC_test.csv")
]

# Loop de construcao do dataset
for (dType, imagePaths, outputPath) in datasets:
	# Abre o CSV de Saida para escrita:
    print("[INFO] construindo arquivo '{}' ...".format(dType))
    f = open(outputPath, "w")

	# Para cada imagem da pasta: 
    for imagePath in imagePaths:
        # Carrega a imagem, formata para 50 x 50 pixels e retorna o array:
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (50, 50))
        image = [str(x) for x in image.flatten()]
        # Extrai a classe a qual esta imagem pertence e
        # Escreve no CSV junto com o array da imagem:
        if imagePath in classZero:
            label = 0
        else:
            label = 1
        f.write("{},{}\n".format(label, ",".join(image)))

    # Fecha o CSV de saida
    f.close()
