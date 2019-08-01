# Detecção de IDC(Carcinoma Ductal Invasivo) com Redes Neurais Convolucionais: Uma comparação entre arquiteturas.

### Este repositório guarda todos os códigos e modelos treinados, bem como informações de ambiente e configuração para reprodutibilidade do trabalho.

![Alt Text](https://www.kaggleusercontent.com/kf/2715518/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..fuWOQXWD1GAhXQ0HgUN1dw.gawyfV8wwN7v_5uJFMZ0hd4Iy_i-St2jH81MwkCQjTb4xl-cr0d91X9mhAWhB4BAHsfugto0njbpt10xl9hZWaiCI0l6o9YOx9ni1gAvBCzxEsvnctT8A8I6N8XFLcvsmRqufjG91JBj1RaoEcVzNlFeOgqTk-cXXl5JZ4gj7oDcQXJ7YXZq5eD1S8Dcu5NN.OrsltsWjeiX7lIYDTRJxKg/__results___files/__results___15_0.png)
***
# Conteúdo:
- ### [Modelos Treinados](https://github.com/otaviomguerra/TCC/tree/master/Modelos%20Treinados): Notebooks, arquitetura detalhada e Plot de Learning Curve de cada arquitetura.
- ### [Notebooks](https://github.com/otaviomguerra/TCC/tree/master/Notebooks): Todos os Notebooks de treinamento das arquiteturas utilizadas e o Notebook de avaliação dos modelos.
- ### [Scripts](https://github.com/otaviomguerra/TCC/tree/master/scripts): Scripts adicionais
***
# Guia de reprodução do processo de treinamento:
 1) Baixar e descompactar [dataset](https://www.kaggle.com/paultimothymooney/breast-histopathology-images).
 2) Executar o script ```make_dataset_csv.py``` na mesma pasta que contém a o diretorio descompactado.
 3) Após isso, utilizar algum dos notebooks das arquiteturas, opcionalmente, fazendo o upload dos CSV's para o [Google Drive](https://drive.google.com/) e utilizando o [Google Colab](https://colab.research.google.com/), ambos serviços gratuitos da Google.
 ***
# Requisitos:
É necessário ter algumas bibliotecas instaladas além do python 3.X padrão para rodar os scripts adequadamente, são elas:
* Keras (Tensorflow backend)
* Numpy
* Matplotlib
* Scikit-Learn
* OpenCV

Para instalar alguma das bibliotecas em uma máquina local é só utilizar o gerenciador de pacotes Pip:

```sh
$ sudo apt install python3-pip
$ sudo pip install <biblioteca>
```

* **OBS:** Em caso de uso do Google Colab não é necessário qualquer instalação de bibliotecas. 
***
# Observação:

### Atentar para os paths dos arquivos CSV durante o processo de treinamento.

