# Cada bloco da memória principal é mapeado em uma única linha da cache
# Para cada bloco na cache, atribui-se um endereço com base no endereço da palavra na memória principal

class BlocoCache:

    # inicializa a cache vazia (apenas o indice e val = 0 )
    def __init__(self, indice):
        self.val = 0  # informação não é válida

        # Endereço gerado pelo processador =  tag + índice

        # ( TAG são os primeiros 2 digitos do endereco)
        self.tag = '--'  # identifica uma informação e é armazenado na cache junto com o conteúdo da posição de memória

        # (Índice são os últimos digitos)
        self.indice = indice  # usado como endereço na cache onde será armazenada a palavra

        self.informacao = '-----'







