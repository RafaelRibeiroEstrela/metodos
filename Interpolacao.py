

import numpy as np
from PIL import Image
import cv2


class Interpolacao:

    def __init__(self):

        self.__diretorio = None
        self.__imagem = None

    def getDiretorio(self):
        return self.__diretorio

    def setDiretorio(self, diretorio):
        self.__diretorio = diretorio

    def getImagem(self):
        return self.__imagem

    def setImagem(self, imagem):
        self.__imagem = imagem
    
    def carregarImagem(self):
        self.__imagem = cv2.imread(self.__diretorio)

    def mostrarImagem(self):
        imagem = cv2.cvtColor(self.__imagem, cv2.COLOR_BGR2RGB)
        cv2.imwrite('saida.png', imagem)
        imagem = Image.open('saida.png')
        imagem.show()

    def aplicarInterpolacao(self, interpolacao):
        self.__imagem = cv2.resize(self.__imagem, None, None, fx = 10, fy = 10, interpolation = interpolacao)
        self.mostrarImagem()





    


