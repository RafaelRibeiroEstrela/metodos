from tkinter import Tk
from tkinter.filedialog import askopenfilename

#FUNÇÃO QUER CARREGA O DIRETÓRIO DO ARQUIVO TEXTO
def carregarArquivo():

    Tk().withdraw()
    diretorio = askopenfilename(title = "SELECIONE A IMAGEM QUE DESEJA FAZER AS OPERAÇÕES")
    return diretorio







