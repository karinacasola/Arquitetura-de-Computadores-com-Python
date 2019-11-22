from BlocoCache import BlocoCache

class MemoriaCache:

    def __init__(self):
        self.tam = 8  # A memória cache deve possuir 8 posições
        # self.blocos = [self.tam]
        self.blocos = {}  # um dicionario para armazenar os blocos com o key indice
        self.inicializar()

    # inicializa a cache vazia (apenas os 8 índices val = 0 )
    def inicializar(self):
        for i in range(8):
            # self.blocos.append(BlocoCache(self.convertBinario(i)))
            indice = str(convertBinario(i))
            self.blocos[indice] = BlocoCache(indice)


    # Verificar se tem cópia da posição de memória correspondente ao endereço
    def buscar(self, endereco):  # buscar os 5 bits na memoria cache simulada
        indice = str(getIndice(endereco))  # Índice últimas 3 posições do endereço
        bloco = self.blocos[indice]  # pega o bloco referente aquele indice

        if self.is_endereco(endereco, bloco):
            return bloco

        # se não está na cache imprime o Miss e retorna -1, para tratamento
        return -1

    # verifica se é o endereço buscado, ou seja se a tag daquele bloco é a mesma do endereço
    def is_endereco(self, endereco, bloco: BlocoCache):
        return bloco.tag == getTag(endereco)

    # copia o dado da memoria principal para a cache
    def copiar(self, endereco):
        indice = getIndice(endereco)
        bloco = self.blocos[indice]  # pega o bloco referente ao indice

        # atualiza as informações
        bloco.val = 1  # informação passa a ser válida
        bloco.tag = getTag(endereco)
        bloco.informacao = endereco


        self.printConteudo(indice)

    # imprime o conteudo da cache destacando a linha que houve alteração
    def printConteudo(self, indice):
        conteudo = "| ind | val | tag | informacao  | \n"
        #print("ind\t| val\t | tag\t | informacao \n")
        for i in self.blocos:
            bloco = self.blocos[i]
            if bloco.indice == indice: # linha da alteração
              conteudo = conteudo + "| " + (bloco.indice) + " |  " + str(bloco.val) + "  | " + str(bloco.tag) + "  | " + trim(str(bloco.informacao)) + " | <--- Alterada \n"
            else:
                conteudo = conteudo + "| " + (bloco.indice) + " |  " + str(bloco.val) + "  | " + str(
                    bloco.tag) + "  | " + trim(str(bloco.informacao)) + " |  \n"

        print(conteudo)


###### ENDEREÇO = TAG(2 primeiros) + ÍNDICE(3 últimos) ######

# TAG as primeiras duas posicoes do endereco
def getTag(endereco):
    return endereco[:2]

# Índice as últimas posicoes do endereco
def getIndice(endereco):
    endereco = trim(endereco)
    return endereco[2:]


# remover o enter
def trim(palavra):
    palavra = palavra.replace('\n', '')
    return palavra

# converte de decimal para binário
def convertBinario(decimal):
    binario = ""
    while decimal > 0:
        # A left shift in binary means /2
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    # preencher com os zeros no inicio
    for i in range(3-len(binario)):
        binario = str(0) + binario
    return binario