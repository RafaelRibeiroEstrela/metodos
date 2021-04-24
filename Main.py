
from DiretorioImagem import carregarArquivo
from Interpolacao import Interpolacao
import cv2


def interpolacaoBicubica(interpolacao):
    interpolacao.aplicarInterpolacao(cv2.INTER_CUBIC)
    interpolacao.carregarImagem()

def interpolacaoLinear(interpolacao):
    interpolacao.aplicarInterpolacao(cv2.INTER_LINEAR)
    interpolacao.carregarImagem()

def carregarImagem(interpolacao, diretorio):
    interpolacao.setDiretorio(diretorio)
    interpolacao.carregarImagem()
    interpolacao.mostrarImagem()


def main():

    diretorio = carregarArquivo()
    interpolacao = Interpolacao()
    carregarImagem(interpolacao, diretorio)


    while (True):
        print ("MENU INTERPOLAÇÃO")
        print ()

        print ("1 - INTERPOLAR POR BICUBICA")
        print ("2 - INTERPOLAR POR BILINEAR")
        print ("0 - SAIR")

        comando = input("DIGITE UM COMANDO VÁLIDO: ")

        if (comando == '0'):
            break

        elif (comando == '1'):
            interpolacaoBicubica(interpolacao)
            print ("\n")

        elif (comando == '2'):
            interpolacaoLinear(interpolacao)
            print ("\n")
        
        else:
            print ("COMANDO INVALIDO !!")
            print ("\n")

    print ("PROGRAMA FINALIZADO !!")


    


    

    


    

    
    
    

    


main()



