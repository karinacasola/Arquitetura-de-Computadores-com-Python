# -*- coding: utf-8 -*-

from MapeamentoDireto import MapeamentoDireto

def main():

    # O  arquivo de entrada “Leituras.txt” contém os endereços
    # dos quais o processador requisita leitura.
    arq = open('Leituras.txt', 'r')
    enderecos = arq.readlines()
    arq.close()

    direto = MapeamentoDireto()
    direto.mapeear(enderecos)

if (__name__ == "__main__"):
    main()




