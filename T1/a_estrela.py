
def ord_key(e):
        return e.custo_total

def valueKey(e):
        return e.value

class ponto:
        x = None                #posicoes [x,y] no mapa
        y = None
        value = None            #valor no mapa (., V, R, M, #, etapas, etc)
        custo_ini = None        #custo desde o inicio
        custo_fim = None        #custo ate o destino, feito pela heuristica
        custo_proprio = None    #custo do anterior para esse ponto
        custo_total = None      #soma dos custos
        anterior = None         #ponto anterior no mapa do qual saimos

        #inicia o ponto
        def __init__(self, x, y, terra_media, anterior):
                self.x = x
                self.y = y
                self.anterior = anterior
                self.value = terra_media.mapa[y][x]
                if anterior == 0:
                        self.custo_proprio = 0
                else:
                        if self.value not in terra_media.custos:
                                self.custo_proprio = 0
                        else:
                                self.custo_proprio = terra_media.custos[self.value]
                

        def soma_custo(self):
                self.custo_total = self.custo_fim + self.custo_ini

        def set_custos(self, destino): #destino eh o ponto de destino da etapa atual
                if self.anterior == 0:
                        self.custo_ini = 0
                else:
                        self.custo_ini  = self.anterior.custo_ini + self.custo_proprio
                
                #metodo de manhattan
                self.custo_fim = abs(self.x - destino.x) + abs(self.y - destino.y)

                self.soma_custo()
        



class terra_media:
        altura = 0
        largura = 0
        ref = None
        reader = None
        mapa = []
        etapas = []
        custos = {
                        '.': 1,
                        'R': 5,
                        'V': 10,
                        'M': 200,
                        'P': float('inf'),
                        '#': float('inf')
        }

        def __init__(self, path):
                self.ref = path

        #funcao que verifica os custos dos vizinhos da primeira casa no aberta
        def analisa_vizinhos(self, tile, etapa, aberta, fechada):
                vizinhos = []
                vizinhos.append(tile)
                #vizinho a frente
                if tile.x < self.largura:
                        vizinho = ponto(tile.x+1, tile.y, self, tile)
                        vizinho.set_custos(self.etapas[etapa])
                        vizinhos.append(vizinho)
                #vizinho atras
                if tile.x > 0:
                        vizinho = ponto(tile.x-1, tile.y, self, tile)
                        vizinho.set_custos(self.etapas[etapa])
                        vizinhos.append(vizinho)
                #vizinho acima
                if tile.y > 0:
                        vizinho = ponto(tile.x, tile.y-1, self, tile)
                        vizinho.set_custos(self.etapas[etapa])
                        vizinhos.append(vizinho)
                #vizinho abaixo
                if tile.y < self.altura:
                        vizinho = ponto(tile.x, tile.y+1, self, tile)
                        vizinho.set_custos(self.etapas[etapa])
                        vizinhos.append(vizinho)

                #verifica se esses vizinhos ja haviam sido checados por outra tile
                podeAdd = True
                for vizi in vizinhos:
                        for point in fechada:
                                if [vizi.x, vizi.y] == [point.x, point.y]:
                                        podeAdd = False
                                        break
                        for point in aberta:
                                if [vizi.x, vizi.y] == [point.x, point.y]:
                                        podeAdd = False
                                        break  
                        if podeAdd:
                                aberta.append(vizi)
                        podeAdd = True

                #retira tile atual do abertas e insere no fechadas
                fechada.append(aberta.pop(0))
                #arruma aberta com as casas de menor custo para ser analisada antes
                aberta.sort(key=ord_key)
                
        #extrai o mapa e criar um dicionario com as coordenadas de cada etapa
        def extrair_mapas(self):
                tiles = set(self.custos.keys())
                self.reader = open(self.ref,"r")
                lines = self.reader.read().splitlines()
                etapas_ind = 0

                for id_y,i in enumerate(lines):
                        self.mapa.append([])
                        for id_x,tile in enumerate(i):
                                self.mapa[id_y].append(tile)
                                if tile not in tiles:
                                        self.etapas.append(ponto(id_x, id_y, self, 0))
                                        self.etapas[etapas_ind].set_custos(self.etapas[etapas_ind])
                                        self.etapas[etapas_ind].soma_custo()
                                        etapas_ind = etapas_ind + 1
                                max_x = id_x            
                        max_y = id_y

                self.altura = max_y 
                self.largura = max_x
                self.etapas.sort(key = valueKey)
                self.reader.close()
                return self.etapas

        def caminho_etapa(self, etapa, aberta, fechada):
                #define inicio e fim da etapa
                if etapa == 0:
                        inicio = self.etapas[17]
                else:
                        inicio = self.etapas[etapa - 1]
                destino = self.etapas[etapa]
                self.analisa_vizinhos(inicio, etapa, aberta, fechada)
                #itera sobre a analisa_vizinhos ate chegar na casa destino
                while [aberta[0].x, aberta[0].y] != [destino.x, destino.y]:
                        self.analisa_vizinhos(aberta[0], etapa, aberta, fechada)
                caminho = []
                atual = aberta[0] #aberta[0] nesse momento eh o destino
                while atual != 0: #volta nos anteriores ate a casa inicial
                        caminho.insert(0, atual)
                        atual = atual.anterior
                #print(caminho[0].x)
                return caminho

        def caminho_alternativo(self, desvio, aberta, fechada):
                if desvio == 1:
                        inicio = self.etapas[9]
                        destino = self.etapas[13]
                        etapa = 13
                else:
                        inicio = self.etapas[12]
                        destino = self.etapas[14]
                        etapa = 14
                print('%c - %c'%(inicio.value, destino.value))
                self.analisa_vizinhos(inicio, etapa, aberta, fechada)
                #itera sobre a analisa_vizinhos ate chegar na casa destino
                while [aberta[0].x, aberta[0].y] != [destino.x, destino.y]:
                        self.analisa_vizinhos(aberta[0], etapa, aberta, fechada)
                caminho = []
                atual = aberta[0] #aberta[0] nesse momento eh o destino
                while atual != 0: #volta nos anteriores ate a casa inicial
                        caminho.insert(0, atual)
                        atual = atual.anterior
                return caminho

        def calcula_caminho(self):
            caminhos = []
            etapa = 0
            aberta = []
            fechada = []

            caminho11 = []
            soma11 = 0
            subEtapa = 10
            while subEtapa < 13:
                    caminho = self.caminho_etapa(subEtapa, aberta, fechada)
                    for tile in caminho:
                            soma11 += tile.custo_proprio
                    aberta = []
                    fechada = []
                    caminho11.append(caminho)
                    subEtapa += 1
                    
            soma14 = 0
            caminho14 = self.caminho_alternativo(1, aberta, fechada)
            for tile in caminho14:
                    soma14 += tile.custo_proprio

            #gera os caminhos de cada etapa e guarda no vetor "caminhos" para facil acesso
            while etapa < 18:
                    aberta = []
                    fechada = []
                    #chega na divisao, ou indo das etapas A, B, C, D para a F (caminho 11), ou saindo de A diretamente para a E (caminho 14)
                    if etapa == 10:
                            if soma14 < soma11:
                                    caminhos.append(caminho14)
                                    etapa = 14
                            else:
                                    for path in caminho11:
                                            caminhos.append(path)
                                    caminho = self.caminho_alternativo(2, aberta, fechada)
                                    caminhos.append(caminho)
                                    etapa = 15
                    else:
                            caminho = self.caminho_etapa(etapa, aberta, fechada)
                            caminhos.append(caminho)
                            etapa += 1
            return caminhos


#middle_earth = terra_media('mapa5.txt')
#middle_earth.extrair_mapas()
#path=middle_earth.calcula_caminho()
#print("caminho")
#print(path[0][0].x)