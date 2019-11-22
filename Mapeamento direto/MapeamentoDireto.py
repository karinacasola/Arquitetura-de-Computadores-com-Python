from MemoriaCache import MemoriaCache
from MemoriaPrincipal import MemoriaPrincipal


class MapeamentoDireto:
    def __init__(self):
        self.principal = MemoriaPrincipal()  # memória principal é criada com os dados do arquivo
        self.cache = MemoriaCache()  # é inicializada vazia
        self.leituras = 0
        self.miss = 0
        self.hits = 0

    # irá mapear os enderecos que o processador requisita leitura.
    def mapeear(self, enderecos):
        for endereco in enderecos:  # Os endereços contêm 5 bits e devem ser buscados na memória cache simulada
            self.leituras = self.leituras + 1
            # Se a tag armazenado no bloco da cache for igual a tag do endereço procurado hit, se não miss
            if self.cache.buscar(endereco) is -1:  # MISS não estava na cache
                print(str(self.leituras) + ": CACHE MISS \n--- Alteração ---")
                self.miss = self.miss + 1

                if self.principal.buscar(endereco) is not -1:  # encontrou na principal, se -1 não encontrou
                     # Tratamento da falta = trazer no nível inferior (memória principal) e armazenar uma copia na cache
                    self.cache.copiar(endereco)
            else:
                print(str(self.leituras) + ": CACHE HIT")
                self.hits = self.hits + 1
        self.imprimirResultado()

    def imprimirResultado(self):
        tx_miss = self.miss / self.leituras
        tx_hits = self.hits / self.leituras

        print("\n### RESULTADOS ###")
        print("Leituras totais: ", self.leituras)
        print("Número de Hits ", self.hits)
        print("Número de Miss: ", self.miss)
        print("Taxa de Hits ", tx_hits)
        print("Número de Miss: ", tx_miss)

