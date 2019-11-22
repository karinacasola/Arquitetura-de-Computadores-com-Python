
import numpy as np

class MemoriaPrincipal:

    def __init__(self):
        self.tam = 32  # A  memória  principal 32  posições
        self.tamBitsPalavra = 16  # Palavras de 16 bits
        self.memoria = np.zeros((self.tam, self.tamBitsPalavra), dtype=int)
        self.inicializar()

    # carrega as palavras do arquivo para a memória principal
    def inicializar(self):
        arq = open('MemoriaPrincipal.txt', 'r')
        conteudo = arq.readlines()
        pos = 0  # regula a posicao da memoria

        for palavra in conteudo:
            for i in range(self.tamBitsPalavra):  # itera os bits
                self.memoria[pos][i] = palavra[i]
          #  print(pos, linha, self.memoria[pos])
            pos = pos + 1  # incrementa contador para setar a proxima posicao da memoria

        arq.close()

    # retorna a palavra contida no endereco passado por parametro
    def buscar(self, endereco):
        posicao = int(converterDecimal(endereco))
        if posicao < 32:
            return self.memoria[posicao]
        else:  # posicao não contida na memoria
            print("A memória principal possui apenas 32 posições. Não possui ", posicao)
            return -1

# converte o endereço de binario para decimal(posicao da matriz)
def converterDecimal(endereco):
    endereco = trim(endereco)
    decimal = 0
    for digito in endereco:  # faz o left shift (x2)
        decimal = decimal * 2 + int(digito)
    return decimal

# remover o enter
def trim(palavra):
    palavra = palavra.replace('\n', '')
    return palavra